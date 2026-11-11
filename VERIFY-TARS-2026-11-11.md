# VERIFY-TARS — تحقق نهائي من التاران قبل الرفع (subagent: VERIFY)

- التاريخ: 2026-11-11 (UTC+02:00 للطوابع الزمنية المحلية)
- الملاك: إنشاء `handoff/_pkg/PACKAGE-LOG.md` §[11] + هذا الملف فقط. قراءة فقط لكل ما سواهما؛ لا شبكة؛ أوامر صغيرة مفردة؛ لا طباعة أي قيمة سرية (بادئات ≤4 محارف فقط عند الضرورة).
- القراءة الأولى: `CONTEXT.md` (116 سطراً) و`AGENTS.md` و`PACKAGE-LOG.md` (ينتهي بـ[10.6]، لا قسم [11]) و`EXCLUDE-LIST.txt` [OBSERVED].
- كل ما في هذا الملف [OBSERVED] بأوامر خرجها مسجل حرفياً، إلا ما وسِم صراحة.

## [V1] المتطلبات — معلومة [10.5] القديمة صارت محدثة [OBSERVED]

CMD: `ls -la --time-style=full-iso /workspace/wiki/work/security-fix-2026-11-10.md`
- الملف موجود الآن: 10,271 بايت، 2026-11-10 09:10:57 → المتطلب (أ) من §[10.6] متحقق [OBSERVED].

CMD: `grep -Ec 'sk-[A-Za-z0-9_-]{16,}' /workspace/wiki/handoff/conversation-export.json`
- الخرج: `0` (grep_exit=1 = لا مطابقات) [OBSERVED].

## [V2] التاران قيد التحقق [OBSERVED]

| الملف | الحجم (بايت) | آخر تعديل |
|---|---|---|
| `wiki-handoff-package.tar.gz` | 61,696,718 | 2026-11-10 22:04:45 |
| `wiki-handoff-light.tar.gz` | 1,742,327 | 2026-11-10 22:04:48 |

ملاحظة: تاريخا البناء (22:04) لاحقان على ملف الإصلاح (09:10) → التاران بُنيا بعد التزكية نظرياً، والإثبات الفعلي في [V4] بالبصمات.

## [V3] فحص عضوية التاران [OBSERVED]

### الحزمة الكاملة
- CMD: `tar -tzf wiki-handoff-package.tar.gz | wc -l` → **202** عضواً.
- CMD: `tar -tzf wiki-handoff-package.tar.gz | grep -Ec 'archive-extract|_pkg|github-release/WIKI_ARCHIVE'` → **0** (grep_exit=1) → الاستثناءات الثلاثة (`archive-extract/`، `handoff/_pkg`، نسخة `github-release/WIKI_ARCHIVE…`) صمدت كلها ✓.
- CMD: `tar -tvzf wiki-handoff-package.tar.gz | grep 'WIKI_ARCHIVE_2026-11-03.tar.gz'`:
  - `-rw-r--r-- box/box 60072453 2026-11-06 19:28 layered-wiki-handoff/WIKI_ARCHIVE_2026-11-03.tar.gz` → الأرشيف الجذري الداخلي بحجمه الدقيق المتوقع 60,072,453 ✓.
  - ولا سطر آخر → لا نسخة github-release داخل الحزمة ✓.
- `tar -tzf … | grep -c 'security-fix-2026-11-10'` → 1 → سجل الإصلاح الأمني داخل الحزمة ✓.

### الحزمة الخفيفة
- CMD: `tar -tzf wiki-handoff-light.tar.gz | wc -l` → **201** عضواً (= 202 − 1).
- نفس نمط الاستثناءات → **0** ✓.
- CMD: `tar -tzf wiki-handoff-light.tar.gz | grep -c 'WIKI_ARCHIVE'` → **0** → لا أرشيف 60MB بأي نسخة ✓.
- `grep -c 'security-fix-2026-11-10'` → 1 ✓.

### إثبات "الخفيف = الكامل ناقص الأرشيف فقط"
- CMD: `diff <(tar -tzf …package… | sort) <(tar -tzf …light… | sort)` → سطر واحد فقط محذوف:
  `< layered-wiki-handoff/WIKI_ARCHIVE_2026-11-03.tar.gz` → لا أي فرق آخر ✓.

## [V4] الطزاجة — sha256 للملفات الستة (المستخرج مقابل الحي) [OBSERVED]

الاستخراج: `mkdir -p verify-full && tar -xzf wiki-handoff-package.tar.gz -C verify-full` (ok)؛ نفسه لـverify-light (ok). جذر الاستخراج في كليهما: `layered-wiki-handoff/`.

المقارنة بـ`cmp -s` لكل ملف من `layered-wiki-handoff/handoff/` مقابل `/workspace/wiki/handoff/`:

| الملف | كامل | خفيف | sha256 الحي (المطابق للمستخرَج في كليهما) |
|---|---|---|---|
| conversation-export.json | **EQUAL** | **EQUAL** | `dbdff76ea0cda13043eda2eb8d6141fa2a3b952b099e5283d68521328d01e49b` |
| MEMORY.md | **EQUAL** | **EQUAL** | `c98665a4d9f73c49aa3531c27e5f8e3be505fdafceabaee64bc5aeba661797d3` |
| README.md | **EQUAL** | **EQUAL** | `4073b60496d645d47f7a6bc05621cd29965e514b7646b056e7c17b17e9195137` |
| CONTEXT.md | **EQUAL** | **EQUAL** | `1ffc5ad53474fc8e9bf3b65c987cc702357492cb4273b6251e6295a8c136efa9` |
| HANDOFF.md | **EQUAL** | **EQUAL** | `c2822e4a44387d11100813ada1d0e7dd9b0c405b59ee896412c02bab03a4d656` |
| WHAT-WAS-DONE.md | **EQUAL** | **EQUAL** | `3d769aaf88b0f3924ce36b3ca0884f123ab2dab7051c5b215fccafb290d43ada` |

- النتيجة: **6/6 EQUAL في كل تار** → التاران يحملان النسخ المصلّحة (طازجة حتى لحظة التحقق 2026-11-11) ✓.
- قرينة إضافية: بصمة `conversation-export.json` الحية `dbdff76e…` ≠ بصمة ما قبل التزكية `142972ea…` المسجلة في §[10.2] → النسخة داخل التارين هي نسخة ما بعد إزالة أسرار `sk-` [OBSERVED].
- قرينة إضافية 2: بصمة `HANDOFF.md` الحية `c2822e4a…` = آخر مزامنة مسجلة في §[08] → لم يتغير منذ 2026-11-09 22:05، فلا تحرير حي بعدها [OBSERVED].
- فحص إضافي بونص: `sha256sum verify-full/layered-wiki-handoff/WIKI_ARCHIVE_2026-11-03.tar.gz` = `e87d82307928bf7a4eebc71b3d4f1419a7f47977ee42e35fa3714375eaee3e16` = نفس بصمة الأرشيف الحي `/workspace/wiki/WIKI_ARCHIVE_2026-11-03.tar.gz` والمسجلة في §[10.1] → العضو الداخلي سليم بالبايت [OBSERVED].

## [V5] المسح الأمني على الشجرتين المستخرجتين [OBSERVED]

CMD (الحرفي المطلوب):
`grep -rEc 'sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{30}' verify-full/ | grep -v ':0$'`
- الخرج: فارغ (exit=1) → **0 ملفات غير صفرية** في الشجرة الكاملة المستخرجة (202 عضواً شاملة work/.log-* و source-transfers) [OBSERVED].
- نفس الأمر على `verify-light/` → فارغ → **0** [OBSERVED].

تصنيف الإصابات:
- إصابات حية (LIVE): **0**.
- أسطر علامات مسبقة التزكية (`[REDACTED-…]`) مطابقة للأنماط: **0** — أي أن الأنماط الموسعة لا تلتقط حتى أسطر العلامات (العلامات لا تطابق البنية `sk-`+16 أو `_`+20).
- → لا عمل إعادة بناء مطلوب.

اختبار سلامة النمط (حتى لا يُخدعنا صمت grep): ملف اصطناعي في `/tmp/opencode` يحوي رمزين مفتعلين (`sk-`+24 و`ghp_`+28) → نفس النمط بـ-E أعطى **2/2** مطابقة ثم حُذف الملف → المسح يعمل فعلية والصفر نتيجة حقيقية [OBSERVED].

مسح الشجرة الحية للمقارنة (بونص): `grep -rEc 'نفس_النمط' /workspace/wiki --exclude-dir=archive-extract --exclude-dir=_pkg | grep -v ':0$'` → فارغ → **0** [OBSERVED].

## [V6] الأحجام مقابل السقف الصلب 104,857,600 بايت [OBSERVED]

| الحزمة | الحجم | نسبة السقف | الهامش |
|---|---|---|---|
| الكامل | 61,696,718 B (58.84 MiB) | 58.84% | **43,160,882 B** (41.16 MiB) ✓ |
| الخفيف | 1,742,327 B (1.66 MiB) | 1.66% | **103,115,273 B** (98.34 MiB) ✓ |

- الحد التحذيري 95×1024×1024 = 99,614,720: الكامل أدناه بهامش 37,918,002 B ✓ [محسوب من القياس].
- بوابة الحجم: SIZE_GATE_PASS لكليهما [OBSERVED].

## [V7] الحكم النهائي

- كل البنود: عضوية (202/201) ✓، استثناءات = 0 ✓، الأرشيف الداخلي 60,072,453 داخل الكامل وغائب عن الخفيف ✓، طزاجة 6/6 EQUAL ×2 ✓، إصابات حية = 0 ✓، الأحجام تحت السقفين ✓.
- حكم القسم [10.6] القديم (FORBIDDEN مشروط) أُلغي بتحقق شرطه (أ) وسَلف شرطاه (ب) عبر بناء 22:04 المُثبت بالبصمات.

**FINAL VERDICT: READY-FOR-UPLOAD** (كلا التارين: `wiki-handoff-package.tar.gz` و`wiki-handoff-light.tar.gz`)

## [V8] التنظيف [OBSERVED]

- CMD: `rm -rf verify-full verify-light` ثم `ls _pkg` — المحاولة الأولى لم تحذفهما (ظلا في القائمة).
- إعادة: `rm -rf /workspace/wiki/handoff/_pkg/verify-full /workspace/wiki/handoff/_pkg/verify-light` → `rm_exit=0`، والقائمة بعدها: `EXCLUDE-LIST.txt، PACKAGE-LOG.md، stage-final، wiki-handoff-light.tar.gz، wiki-handoff-package.tar.gz` → التنظيف تم ✓.
- `stage-final/` موجود مسبقاً داخل _pkg (قبل هذه الجلسة) — لم يُلمس ولا فُحص محتواه (خارج النطاق).
