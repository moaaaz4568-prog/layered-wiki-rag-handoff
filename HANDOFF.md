# handoff/HANDOFF.md — الملف الرئيسي للتسليم (Master Handoff)

> **التاريخ:** 2026-11-09 · **الكاتب:** وكيل فرعي يملك هذا الملف وحده.
> **الوسوم الإجبارية:** `OBSERVED` · `REPORTED` · `PROPOSED` · `UNKNOWN` · `NOT_RUN`. [REPORTED — repo/AGENTS.md]
> **السرية:** لا قيمة مفتاح هنا؛ المفتاح المكشوف = `[REDACTED-PAT-40chars-ROTATE-REQUIRED]` فقط. ممنوع طباعة أي توكن (أمر/رابط/ردّ). [REPORTED — work/secrets-2ndpass-2026-11-07.md §1]
> **البيئة:** بلا شبكة؛ `repo/` بلا `.git`. [OBSERVED — `test -d repo/.git` = no]

## 1) المهمة الجارية الآن — الحقائق الأساسية

| الحقيقة | القيمة | الأمر/المصدر | الوسم |
|---|---|---|---|
| صفوف `repo/MESSAGES.md` | **57 من 106** (فجوة 49) | `grep -c '^| [0-9]' /workspace/wiki/repo/MESSAGES.md` = **57** | `OBSERVED` (57) / `REPORTED` (106) |
| ملفات repo محلياً | **42** | `find repo -type f \| wc -l` = **42** | `OBSERVED` |
| HEAD البعيد | شجرة `37ad6448…036` بها **60** ملفاً (فارق 18)؛ آخر دفعة `5b70e59..79480a3 main` | `work/remote-tree-2026-11-05/-06.json` + `work/upload-report.md:3,11` | `REPORTED` |
| التوكن المكشوف سابقاً | 6 مواضع معتمة؛ إبطاله على الخادم **لم يثبت** | `work/.log-analysis-session-b:74` + `work/.log-session-c:71,807,915,935,967` | تدويره `UNKNOWN` — يدوي للمستخدم (GitHub → Settings → Developer settings → PATs) |

> **المحصلة:** الحارق = إنهاء MESSAGES إلى 106 (T1/K1)؛ 5 محاولات انقطعت. [REPORTED — WHAT-WAS-DONE.md §9]

## 2) الخطوات التالية بالترتيب (أمر تحقق + المتوقع)

| # | الخطوة | الأمر والتحقق | المتوقع | الحالة |
|---|---|---|---|---|
| 1 | فحص بيئة الجهاز الجديد | `for t in git jq python3 tar; do command -v $t >/dev/null && echo "$t: yes" \|\| echo "$t: NO"; done` | **4× yes** (القديم: موجودة + gh) | `NOT_RUN` الجديد / `OBSERVED` القديم |
| 2 | بصمة التار | `sha256sum WIKI_ARCHIVE_2026-11-03.tar.gz` | `e87d82307928bf7a4eebc71b3d4f1419a7f47977ee42e35fa3714375eaee3e16` بـ60,072,453 بايتاً و3,664 مدخلاً | [OBSERVED اليوم] |
| 3 | **إنهاء MESSAGES.md إلى 106** (T1) | المصادر: `work/msg-anchor-index.md` (106) + `work/msg-ext-01..08.md` (8 ملفات/726 سطراً) + `source-transfers/wiki_all_talk.md` (2,012 سطراً/106)؛ الملف الوحيد المعدّل: `repo/MESSAGES.md` | `grep -c '^| [0-9]' repo/MESSAGES.md` = **106** (K1)؛ و`find repo -name '*.md' \| wc -l` ≥ 36 (K7) | `NOT_RUN` — تضارب msg-ext (MEMORY=815/قياسي=**726**)؛ الأحدث يفوز، وإن اختلفت المراسي قف ووثّق |
| 4 | تحقق YAML والروابط | YAML: `python3 -c "import yaml,glob; [yaml.safe_load(open(f)) for f in glob.glob('/workspace/wiki/repo/config/*.yaml')]; print('yaml-ok')"` — روابط: `grep -rEo '\]\([^)]+\)' repo --include='*.md' \| grep -v http \| wc -l` ثم فحص كل هدف | `yaml-ok` لـ4 config (K5)؛ **صفر** رابط مكسور (K6)؛ 6 null في `thresholds.yaml:9-14` تظل حتى D3 | `NOT_RUN` (yaml غائبة) |
| 5 | رفع الإصلاحات إلى GitHub | قبل الدفع: `grep -rEln 'ghp_[A-Za-z0-9]{8}\|github_pat_[A-Za-z0-9_]{8}' repo` ← **صفر** (K3). التوكن ترويسة Authorization/`GIT_ASKPASS` **فقط** — لا قرص/URL/سطر أمر | دفع `main -> main`؛ تحقق `git ls-remote` بترويسة؛ البعيد الآن `37ad644` [REPORTED] | `NOT_RUN` — **لا رفع دون إذن مستخدم صريح + توكن شغّال** [REPORTED — README §(e)3] |
| 6 | الدورات 2–4 | تُستخرج مهامها من `work/plan-cycle-02.md` (T2–T10 + K1–K12) بعد 1–5 | لا `work/review-5..8` قبل الانتهاء (K9) | `NOT_RUN` — لا إطلاق قبل D6 [REPORTED — §5] |

## 3) كيف تعمل — بروتوكول التشغيل

- **موجات صغيرة:** 5–6 وكلاء كحد أعلى؛ موجات ≥10 انهارت: قص بلا `finish_reason`/`ECONNRESET`/`aborted`/HTTP 522/حدّ مجاني 429 — نجاح ≈ 0%. [PROPOSED الحد / REPORTED الانهيارات — MEMORY.md §4 + WHAT-WAS-DONE §9]
- **ملكية ملف وحيد:** كل مهمة تعدّل ملفاً واحداً وتُسجّل في T10. [REPORTED — plan-cycle-02 §3]
- **الرد بالعربية:** والمصطلح العلمي بالإنجليزية عند أول ذكر. [REPORTED — البريف س19–20]
- **وسم كل ادعاء** بالوسوم الخمسة، و**قِس قبل أن تُعلن**: كل رقم بأمر قياس أو يوسم تقديراً؛ ما لم يُقرأ = UNKNOWN. [REPORTED — repo/AGENTS.md + RULES.md ق5]
- **الأسرار:** لا قيمة تُطبع؛ الإبلاغ: `file:line` + أول 8 محارف. [REPORTED — secrets-2ndpass §1]
- **`repo/` بلا `.git`:** تعديل محلي كمرآة؛ لا دفع دون إذن صريح. [OBSERVED — `test -d repo/.git` = no]
- وأماناً إضافياً: `archive-extract/` عدّ فقط؛ وراجع `repo/.gitignore` قبل كل commit — تفصيل README §(e)4–6. [REPORTED]

## 4) ستة قرارات محبوسة على المستخدم — كلها `UNKNOWN / awaiting-user`

| # | القرار | البدائل | المصدر |
|---|---|---|---|
| D1 | حجر التناقض مقابل عرض الطرفين («مفيش حجر خالص» البريف س3) | حجر ميكانيكي فقط · عرض الطرفين · هجين موسوم | CONTRADICTION-POLICY.md + البريف س84–87 [REPORTED] |
| D2 | حدّ «الرأي الغبي جداً / خارج المجال» — الاستثناء الوحيد للحذف، «أخطر قرار» | تعريف دلالي · لائحة · لجنة بشرية | promptastra6fgss.md:239 + RULES.md ق2 [REPORTED] |
| D3 | قيمة k (Top-k) والعتبات | ثابتة · null حتى أول قياسين · متعددة | `thresholds.yaml:9-14` = **6 null**: top_k، recall_at_k، recall_target، answer_latency_max_s، rerank_latency_max_s، faithfulness_min [OBSERVED] |
| D4 | خاص مقابل عام («مفيش نشر» البريف س11) | بقاء خاص · عام · README فقط؛ ومستودع الحزمة طُلب «public» ولم يُنشأ | البريف س11 + repo-plan-01.md §1.2.1 + conversation-export.md:4648 [REPORTED/`NOT_RUN`] |
| D5 | تدوير PAT | تدوير موثق · عدم التدوير مع تبرير | الإبطال على الخادم `UNKNOWN` — يدوي للمستخدم [OBSERVED غياب التأكيد] |
| D6 | إطلاق الدورة 2 | الآن · بعد D1–D5 · إلغاء الدورات 2–4 | plan-cycle-02 §5-D6 — بلا ردّ: القياسات فقط [REPORTED] |

## 5) أين تقرأ أولاً — تسلسل القراءة للجلسة الجديدة

**1)** `handoff/README.md` (13,279B؛ تضارب 9,502 — الأحدث يفوز) — التهيئة والتحذيرات (a)–(e)؛ **2)** `handoff/CONTEXT.md` (26,857B) — الهدف والقواعد والأرقام والتناقضات؛ **3)** `handoff/MEMORY.md` (18,219B) — المنجز والأرقام والانكسارات؛ **4)** `handoff/WHAT-WAS-DONE.md` (26,035B) — السرد الزمني + الفجوات الـ13؛ **5)** هذا الملف — الموجز التشغيلي؛ **6)** `handoff/conversation-export.md` (342,272B/4,786 سطراً/223 رسالة/40 إخفاءً) و`.json` (1,709,588B) للنص الحرفي عند الحاجة.

ثم للعمل: `AGENTS.md` ← `repo/README.md` ← `work/plan-cycle-02.md`؛ وعند تضارب ملفين يفوز القياس المؤرَّخ الأحدث. [REPORTED — README §(c)]

---

> **القياس النهائي:** 8170 بايت (`wc -c` — 2026-11-09). الهدف <8KB والدقة أولاً؛ لا سرّيات ولا شبكة.
