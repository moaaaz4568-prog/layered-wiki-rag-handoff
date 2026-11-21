#!/usr/bin/env python3
"""Incremental Drive upload for the SECOND Muse account (wiki build).

Adapted from the first side's drive_sync.py. Same sync logic:
walk the work trees, upload new files, update changed ones (by
size+mtime), skip unchanged ones, never upload secrets.

WHAT IS DIFFERENT HERE (read this before running):
1. Paths: fill in WORKSPACE_ROOT for YOUR disk layout below. Do NOT
   assume the first side's /home/hatch paths.
2. Drive folder: fill in DRIVE_FOLDER_ID with the SHARED folder id
   معاذ shares with you (NOT the first side's Muse-Backup folder).
3. Drive backend: the first side uses /opt/hatch/bin/hatch_gws_cli,
   which exists only on its VM. Wire the three adapter functions
   (drive_create_file, drive_update_file, drive_create_folder) to
   YOUR Drive tool: your google_drive connector CLI, an rclone remote,
   or the Drive API. The rest of this script (walk / exclude / state /
   retry / logging) works unchanged once the adapter is wired.

Run repeatedly (cron every 5 minutes). State (local path -> Drive file
id, size, mtime; plus folder id cache) is kept in
drive-sync-state.json next to this script.

Exclusions (never uploaded): .env*, *secret*, *.pem, *.key,
*credential*, *.db, *.onnx, .git, .venv, node_modules, __pycache__,
models/, sources/ under knowledge-forge namespaces, wiki-handoff tars.
"""
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ==================== CONFIG — FILL IN BEFORE FIRST RUN ====================
# Your workspace root on YOUR disk (where you cloned knowledge-forge).
WORKSPACE_ROOT = Path(os.environ.get(
    "SECOND_MUSE_WORKSPACE", "/path/to/your/workspace"))
# The shared Drive folder id معاذ shares with you (from its share link).
DRIVE_FOLDER_ID = os.environ.get("SECOND_MUSE_DRIVE_FOLDER_ID", "")
# How to reach Drive from this machine. Options:
#   "gws"    -> hatch_gws_cli (only if it exists on your machine)
#   "rclone" -> rclone remote named in RCLONE_REMOTE (e.g. "gdrive:")
#   "custom" -> implement the three adapter functions below yourself
DRIVE_BACKEND = os.environ.get("SECOND_MUSE_DRIVE_BACKEND", "custom")
RCLONE_REMOTE = os.environ.get("SECOND_MUSE_RCLONE_REMOTE", "gdrive:")
GWS = "/opt/hatch/bin/hatch_gws_cli"
# ============================================================================

STATE_JSON = Path(__file__).resolve().parent / "drive-sync-state.json"
LOG = Path(__file__).resolve().parent / "drive-sync.log"
MAX_WORKERS = 8
RETRIES = 3

# (local root, drive-relative dir) — directory trees to walk.
# ADJUST these to your disk: keep the drive-relative names the same so
# the Drive layout matches the first side's layout.
DIR_ROOTS = [
    (WORKSPACE_ROOT / "knowledge-forge/namespaces/social-ar/atoms",
     "workspace/knowledge-forge/namespaces/social-ar/atoms"),
    (WORKSPACE_ROOT / "knowledge-forge/namespaces/social-en/atoms",
     "workspace/knowledge-forge/namespaces/social-en/atoms"),
    (WORKSPACE_ROOT / "knowledge-forge/.work",
     "workspace/knowledge-forge/.work"),
    (WORKSPACE_ROOT / "knowledge-forge/tools",
     "workspace/knowledge-forge/tools"),
    (WORKSPACE_ROOT / "knowledge-forge/docs",
     "workspace/knowledge-forge/docs"),
    (WORKSPACE_ROOT / "second-muse-handoff",
     "workspace/second-muse-handoff"),
]
# individual files: (local path, drive-relative path)
FILES = [
    (WORKSPACE_ROOT / "knowledge-forge/AGENTS.md",
     "workspace/knowledge-forge/AGENTS.md"),
    (WORKSPACE_ROOT / "knowledge-forge/LOG.md",
     "workspace/knowledge-forge/LOG.md"),
    (WORKSPACE_ROOT / "knowledge-forge/README.md",
     "workspace/knowledge-forge/README.md"),
]

EXCLUDE_DIRS = {".git", ".venv", "node_modules", "__pycache__", ".models",
                ".kforge", "sources", "models"}
EXCLUDE_SUFFIXES = {".db", ".db-journal", ".db-wal", ".db-shm", ".onnx",
                    ".pyc"}
EXCLUDE_NAMES = {"wiki-handoff-package.tar.gz", "wiki-handoff-light.tar.gz"}
EXCLUDE_SUBSTR = {".env", "secret", ".pem", ".key", "credential"}


def log(msg):
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


# ==================== DRIVE ADAPTER — WIRE TO YOUR TOOL ====================
def drive_create_folder(name, parent_id):
    """Create a Drive folder; return its Drive file id."""
    if DRIVE_BACKEND == "gws":
        r = subprocess.run(
            [GWS, "drive", "files", "create",
             "--params", '{"ignoreDefaultVisibility":true}',
             "--json", json.dumps({
                 "name": name,
                 "mimeType": "application/vnd.google-apps.folder",
                 "parents": [parent_id]})],
            capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            raise RuntimeError(f"gws create folder failed: "
                               f"{(r.stdout + r.stderr)[:500]}")
        return json.loads(r.stdout)["id"]
    if DRIVE_BACKEND == "rclone":
        dest = f"{RCLONE_REMOTE}{name}/"
        r = subprocess.run(["rclone", "mkdir", dest],
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            raise RuntimeError(f"rclone mkdir failed: {r.stderr[:500]}")
        # rclone has no stable file ids; use the path as the id.
        return dest
    raise NotImplementedError(
        "DRIVE_BACKEND=custom: implement drive_create_folder() with your "
        "Drive tool (connector CLI or API), then set DRIVE_BACKEND "
        "accordingly.")


def drive_create_file(local: Path, parent_id, name):
    """Upload a new file; return its Drive file id (or path for rclone)."""
    if DRIVE_BACKEND == "gws":
        r = subprocess.run(
            [GWS, "drive", "files", "create",
             "--params", '{"ignoreDefaultVisibility":true}',
             "--json", json.dumps({"name": name, "parents": [parent_id]}),
             "--upload", str(local)],
            capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            raise RuntimeError(f"gws create file failed: "
                               f"{(r.stdout + r.stderr)[:500]}")
        return json.loads(r.stdout)["id"]
    if DRIVE_BACKEND == "rclone":
        dest = f"{RCLONE_REMOTE}{parent_id}{name}"
        r = subprocess.run(["rclone", "copyto", str(local), dest],
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            raise RuntimeError(f"rclone copyto failed: {r.stderr[:500]}")
        return dest
    raise NotImplementedError(
        "DRIVE_BACKEND=custom: implement drive_create_file() with your "
        "Drive tool.")


def drive_update_file(local: Path, drive_id, parent_path=""):
    """Replace the content of an existing Drive file."""
    if DRIVE_BACKEND == "gws":
        r = subprocess.run(
            [GWS, "drive", "files", "update",
             "--params", json.dumps({"fileId": drive_id}),
             "--upload", str(local)],
            capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            raise RuntimeError(f"gws update failed: "
                               f"{(r.stdout + r.stderr)[:500]}")
        return drive_id
    if DRIVE_BACKEND == "rclone":
        dest = drive_id  # for rclone the id IS the destination path
        r = subprocess.run(["rclone", "copyto", str(local), dest],
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            raise RuntimeError(f"rclone copyto failed: {r.stderr[:500]}")
        return dest
    raise NotImplementedError(
        "DRIVE_BACKEND=custom: implement drive_update_file() with your "
        "Drive tool.")
# ================== END OF ADAPTER — REST IS BACKEND-FREE ==================


def is_excluded(path: Path) -> bool:
    name = path.name
    low = name.lower()
    if path.suffix.lower() in EXCLUDE_SUFFIXES:
        return True
    if name in EXCLUDE_NAMES:
        return True
    if any(s in low for s in EXCLUDE_SUBSTR):
        return True
    return False


def collect():
    """Return list of (local Path, drive-relative path)."""
    items = []
    for local_root, drive_rel in DIR_ROOTS:
        if not local_root.exists():
            log(f"WARN root missing: {local_root}")
            continue
        for dirpath, dirnames, filenames in os.walk(local_root):
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
            for fn in filenames:
                p = Path(dirpath) / fn
                if is_excluded(p):
                    continue
                rel = p.relative_to(local_root)
                items.append((p, f"{drive_rel}/{rel}"))
    for local_path, drive_rel in FILES:
        if local_path.exists() and not is_excluded(local_path):
            items.append((local_path, drive_rel))
    seen = set()
    out = []
    for p, d in items:
        key = str(p)
        if key in seen:
            continue
        seen.add(key)
        out.append((p, d))
    return out


def load_state():
    if STATE_JSON.exists():
        try:
            return json.loads(STATE_JSON.read_text())
        except Exception:
            pass
    return {"folders": {}, "files": {}}


def save_state(state):
    STATE_JSON.write_text(json.dumps(state, indent=1, sort_keys=True))


def ensure_folder(state, drive_rel_dir):
    """Create (or reuse) the Drive folder for a relative dir path.
    SINGLE-THREADED ONLY — call before starting the worker pool."""
    if drive_rel_dir in state["folders"]:
        return state["folders"][drive_rel_dir]
    parts = drive_rel_dir.split("/")
    parent = DRIVE_FOLDER_ID
    cur = ""
    for part in parts:
        cur = f"{cur}/{part}" if cur else part
        if cur in state["folders"]:
            parent = state["folders"][cur]
            continue
        folder_id = drive_create_folder(part, parent)
        state["folders"][cur] = folder_id
        parent = folder_id
        save_state(state)
    return state["folders"][drive_rel_dir]


def precreate_folders(state, items):
    dirs = sorted({d.rsplit("/", 1)[0] for _, d in items if "/" in d})
    for d in dirs:
        ensure_folder(state, d)
    log(f"folders ready: {len(state['folders'])}")


def upload_one(state, local: Path, drive_rel: str):
    """Upload new file or update changed one. Does NOT mutate state;
    returns (action, bytes, drive_id)."""
    st = os.stat(local)
    key = str(local)
    prev = state["files"].get(key)
    if prev and prev.get("size") == st.st_size and prev.get("mtime") == st.st_mtime:
        return ("skip", 0, prev.get("drive_id"))
    drive_dir = drive_rel.rsplit("/", 1)[0] if "/" in drive_rel else ""
    name = local.name
    if prev and prev.get("drive_id"):
        for attempt in range(RETRIES):
            try:
                drive_update_file(local, prev["drive_id"], drive_dir)
                break
            except Exception:
                if attempt == RETRIES - 1:
                    raise
                time.sleep(2 ** attempt)
        return ("update", st.st_size, prev["drive_id"])
    parent = state["folders"][drive_dir] if drive_dir else DRIVE_FOLDER_ID
    for attempt in range(RETRIES):
        try:
            drive_id = drive_create_file(local, parent, name)
            break
        except Exception:
            if attempt == RETRIES - 1:
                raise
            time.sleep(2 ** attempt)
    return ("upload", st.st_size, drive_id)


def main():
    if not DRIVE_FOLDER_ID:
        print("ERROR: set DRIVE_FOLDER_ID (env SECOND_MUSE_DRIVE_FOLDER_ID "
              "or edit the CONFIG block at the top of this script).",
              file=sys.stderr)
        return 2
    if not WORKSPACE_ROOT.exists():
        print(f"ERROR: WORKSPACE_ROOT does not exist: {WORKSPACE_ROOT}",
              file=sys.stderr)
        return 2
    log("=== drive sync start ===")
    state = load_state()
    items = collect()
    log(f"manifest: {len(items)} files")
    precreate_folders(state, items)
    counts = {"upload": 0, "update": 0, "skip": 0, "error": 0}
    bytes_up = 0
    errors = []

    def prio(d):
        if "/atoms/" in d or d.endswith("LOG.md"):
            return 0
        if "/.work/" in d:
            return 0
        return 1

    items.sort(key=lambda t: (prio(t[1]), t[1]))
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(upload_one, state, p, d): (p, d) for p, d in items}
        done = 0
        for fut in as_completed(futs):
            p, d = futs[fut]
            done += 1
            try:
                action, nbytes, drive_id = fut.result()
                counts[action] += 1
                bytes_up += nbytes
                if action in ("upload", "update") and drive_id:
                    st = os.stat(p)
                    state["files"][str(p)] = {
                        "drive_id": drive_id, "size": st.st_size,
                        "mtime": st.st_mtime, "drive_rel": d}
            except Exception as e:
                counts["error"] += 1
                errors.append(f"{p}: {e}")
                log(f"ERROR {p}: {e}")
            if done % 200 == 0:
                log(f"progress {done}/{len(items)} "
                    f"up={counts['upload']} upd={counts['update']} "
                    f"skip={counts['skip']} err={counts['error']}")
                save_state(state)
    save_state(state)
    log(f"=== done: {counts} bytes_uploaded={bytes_up} errors={len(errors)}")
    for e in errors[:20]:
        log(f"  ERR {e}")
    return 0 if counts["error"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
