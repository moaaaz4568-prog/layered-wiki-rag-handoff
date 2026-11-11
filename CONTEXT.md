# handoff/CONTEXT.md — السياق المرجعي الرسمي للجلسة الجديدة (layered-wiki-rag)

> **التاريخ:** 2026-11-09.
> **الكاتب:** وكيل فرعي (subagent). ملكه هذا الملف وحده، لم يعدّل غيره.
> **دور الملف:** مرجع السياق المعتمد للجلسة الجديدة على الحاسوب الآخر. إذا تعارض ملف آخر في handoff/ مع هذا الملف، تُعتمد هنا ما هي موثّقة بالأمر والتاريخ، ويُعلَن الفارق قبل أي قرار. [PROPOSED — المصدر: handoff/README.md §(c) يطلب ملف سياق يكفي للتوجيه]
> **قاعدة كل سطر أدناه:** وسم دليل إلزامي: OBSERVED أو REPORTED أو PROPOSED أو UNKNOWN أو NOT_RUN + المصدر. كل OBSERVED هنا قيست أو قُرئت مباشرة بتاريخ 2026-11-09 بأمر مذكور، إلا إن ذُكر تاريخ آخر. [REPORTED — repo/AGENTS.md «أدلة وتحقق»]
> **سريات:** لا قيمة مفتاح في هذا الملف. أي إشارة لمفتاح GitHub المكشوف تُكتب بالبديل النصي `[REDACTED-PAT-40chars-ROTATE-REQUIRED]` فقط. [OBSERVED — التزام هذه الجلسة بـ work/secrets-2ndpass-2026-11-07.md §1]
> **لا شبكة في جلسة الكتابة هذه، ولا git محلي.** كل قياس هنا من القرص المحلي فقط. [OBSERVED]

## 1) الهدف ومعايير النجاح

- الهدف: إخراج «عقول متخصصة في جانب واحد». مثال معاذ: من ويكي بزنس تُستخرج معرفة bizness models وoutreach، ثم يقول للنموذج «اعمل بزنس بلان» فيجيب بعلم المجال كله. ومن هنا فكرة الماسترز: مصطلحات، ثم مجلد موضوع، ثم ملف ماستر رئيسي بإحالات إلى ماسترز فرعية بمسارات واضحة. [REPORTED — المصدر: /workspace/promptastra6fgss.md سطرا 1 و7]
- قاعدة معاذ المزدوجة الحرفية: «مفيش حجر خالص، ونعرض الطرفين دايماً». [OBSERVED — البريف سطر 3]
- المستفيد: أي محادثة AI جديدة تفهم المشروع من المستودع دون إعادة قراءة الأرشيف. والنماذج الأخرى تدرس بنية الماسترز وتبني أنظمة بنفس التفكير وتطور عليه. [REPORTED — البريف سطر 1 + repo/README.md §1 و §4]
- معايير النجاح: الأهداف الخمسة في repo/docs/GOALS.md §2 (رؤية باستشهاد بالمقطع الخام، تحديد بفلتر الشخصية الإجباري، إجابة من مقاطع فقط، صوت المنظور من مقاطعه، ثقة بمراجعة بشرية) + «يُحظر إعلان DONE قبل 4 مراجعات». [OBSERVED — قراءة repo/docs/GOALS.md و repo/docs/RULES.md §5]
- النجاح المقاس الوحيد على القرص: BM25 على 210 صفحات هيثم: 12/15 في المرتبة الأولى، 14/15 في أول 3، أسئلة العناوين 8/8، الصياغات المختلفة 1/3 فقط (أحدها مرتبة 28 وآخر 35). الفجوة = صياغات عامة مشتركة الكلمات، وعلاجها تضمين كثيف وإعادة ترتيب: NOT_RUN. [REPORTED — work/analysis-wiki-talk-01.md §1.10 + repo/CONTEXT.md §4]
- الحالة: الدورة 1 مكتملة ومرفوعة (commit 79480a3). الدورات 2–4 كلها NOT_RUN. تقدير الجلسة الأم للإنجاز ~70/100 (تقدير موثق، ليس رقما مخترعا هنا). [REPORTED — handoff/conversation-export.md جدول «ما لم يتحقق» + work/plan-cycle-02.md §6]

## 2) هرمية القواعد والإلزاميات

- ترتيب الحاكمية: **pro.md ثم AGENTS.md ثم RULES.md**. الموجه: pro.md أحدث كلام مباشر من معاذ (2026-11-03)، وكلام معاذ المباشر يفوق أي مستند في الجلسة؛ ثم تعليمات الوكلاء الدائمة؛ ثم مستند القواعد داخل repo. [REPORTED — استنتاج منهجي؛ الأساس الأول: قول AGENTS.md «لا تخمن السياق؛ استخدم ما هو موثق»، والأساس الثاني: أن كلام معاذ المباشر أنجز تغييرات فعلية عند صدورها، منها تحديث ملف تعليمات كلود بالرسالة 94 «ضيف الكلام ده لملف كلود» والرسالة 17 «امسح الكوكيز وامسح توكن جيت»]
- **pro.md** (ملف واحد طويل، 2026-11-03): «make this missy thing organized»، «build me this thing like a github repo»، «explore and search then plan then execute then review then repeat this 4 times»، «use sub agents dont ever work by yourself»، «search on x.com, reddit, github»، + 3 روابط: transfernow ×2 وgithub release v1.0.0. [OBSERVED — قراءة /workspace/wiki/source-transfers/20261103BdZVc6uf/pro.md كاملاً]
- **AGENTS.md** (repo/AGENTS.md): اقرأ CONTEXT.md أولاً ثم AGENTS.md؛ sub-agents دائماً والمشرف يخطط ويراجع فقط؛ لا تخمن السياق؛ الوسوم الخمسة إجبارية؛ لا ادعاء نجاح غير مختبر؛ لا أسرار أبداً؛ المستودع خاص ولا يجعله عاماً دون إذن صريح؛ .env.example نصوص فارغة؛ فحص .gitignore قبل كل commit؛ التغييرات صغيرة ووثّق ما لم يُختبر؛ الأولوية: السلامة ثم الخصوصية ثم الإنجاز. [OBSERVED — قراءة كاملة]
- **RULES.md = 13 قاعدة مرقّمة + 12 قاعدة مكمّلة = 25** (عنوان الملف حرفياً). أهمّها: (1) كل ملف يدخل بكل محتواه، والاستثناء الوحيد «رأي غبي جداً أو خارج المجال يُحذف كاملاً»؛ (3) مصطلحات أولاً ثم ماستر، والنقل لا الحذف r→done→processed؛ (4) كل عملية بنظام حرفي: وكلاء تعملون والمشرف يخطط ويوجه ويفحص؛ (5) كل رقم له أمر قياس أو يُوسم تقديراً، وما لم يُقرأ UNKNOWN؛ (6) لا إصلاح ولا ادعاء قبل فحص القرص؛ (7) لا قيم مخزنة، متغير بيئة فقط؛ (8) الخام للقراءة فقط؛ (9) الترقية بموافقة إنسان scratch→research→candidate→canon؛ (10) لا توسع على فشل؛ (11) لا تضمين قبل اختبار (bge-m3 مرشح مشروط)؛ (12) المقطع = عنوان/فقرة أو نطاق محارف أو جدول/قائمة، لا تقطيع أعمى؛ (13) فلتر الشخصية إجباري كبيانات وصفية لا كوزن تشابه. [OBSERVED — قراءة repo/docs/RULES.md §1–§5]
- العرض: **الرد بالعربية**، والمصطلح العلمي بالإنجليزية بين قوسين عند أول ذكر، بلا تشبيهات أو قصص. [REPORTED — البريف سطرا 19–20 + work/analysis-session-01.md §1]
- الرقم أو الاقتباس بلا مصدر مرفوض. [REPORTED — repo/docs/RULES.md القاعدة 5]

## 3) الأرقام المرجعية (canonical numbers)

| الرقم | القيمة | الوسم | الأمر / المصدر |
|---|---|---|---|
| صفحات الست ويكيات | 5,896 صفحة / 31.3MB = 31,262,266 بايت | REPORTED | work/analysis-wiki-talk-01.md §1.7 + repo/CONTEXT.md §2 |
| مصطلحات wikillm مقابل الماسترز | 27,742 ذرة مقابل 5 ماسترز = خرق «مصطلحات قبل ماستر» | REPORTED | work/analysis-wiki-talk-01.md §2.4 |
| Infinite Brain OS | 584 ملفاً / 4.7MB، المدقق ناجح على 228 عقدة | REPORTED | work/analysis-wiki-talk-01.md §2.5 |
| رسائل «كلام الويكي» | 106 رسائل في 2,012 سطراً، متسلسلة 1..106 بلا فجوات | OBSERVED اليوم | `grep -cE '^## [0-9]+ — ' source-transfers/wiki_all_talk.md` = 106؛ `wc -l` = 2,012؛ المراسي في work/msg-anchor-index.md |
| أرشيف الويكي الكامل | 2,713 ملفاً / 212MB | REPORTED | work/archive-inventory-01.md §2. تناقض اليوم: الاستخراج المحلي فيه 2,685 ملفاً (`find archive-extract -type f | wc -l`)، فارق 28 غير محسوم — توقف ووثّقه قبل الاعتماد |
| ملفات repo محلياً | 42 ملفاً (13 جذر + config 4 + docs 11 + index 2 + masters 2 + reference 2 + sources 5 + templates 2 + timeline 1)، منها 36 ملفاً .md | OBSERVED اليوم | `find repo -type f | wc -l` = 42؛ `find repo -name '*.md' | wc -l` = 36 |
| صفوف MESSAGES.md | 57 صف بجدول رقمي (الهدف 106؛ الفجوة 49) | OBSERVED اليوم | `grep -c '^| [0-9]' repo/MESSAGES.md` = 57 |
| ملفات repo في HEAD البعيد | 60 blob؛ شجرة 37ad6448…؛ سجل الدفع 79480a3… (5b70e59..79480a3 main) | REPORTED | work/upload-report.md سطرا 3 و5 و11 + work/remote-tree-2026-11-05.json و -06.json (72 مدخلاً / 60 blob غير مقصوصة) |
| الأرشيف المضغوط | WIKI_ARCHIVE_2026-11-03.tar.gz = 60,072,453 بايت، 3,664 مدخلاً؛ نسختان متطابقتان بالبتات (الجذر + source-transfers/github-release/) | OBSERVED اليوم | `ls -l` + `tar -tzf \| wc -l` + `cmp` |
| بصمة sha256 للأرشيف | e87d82307928bf7a4eebc71b3d4f1419a7f47977ee42e35fa3714375eaee3e16 | OBSERVED اليوم | `sha256sum /workspace/wiki/WIKI_ARCHIVE_2026-11-03.tar.gz` |
| تصدير المحادثة الأم | handoff/conversation-export.md = 342,272 بايت / 4,786 سطراً / 223 رسالة / 40 إخفاء؛ JSON = 1,709,609 بايت قياس 2026-11-10 (كان 1,709,588 في 2026-11-09 وتغير لحظياً 09:06) / 74 إخفاء بالنمط `[REDACTED` (بالأمر المدوَّن `grep -c REDACTED` = **75** سطراً و87 تكراراً — تصحيح 2026-11-10) | OBSERVED اليوم | `wc -l` + `ls -l` + `grep -c REDACTED` + ترويسة التصدير (الإنتاج: `opencode session export`، الجلسة ses_e579b7fdaffeAHx1JmbPoKB7dI بنعنوان PONG) |
| امتدادات msg-ext | 8 ملفات نسخ حرفي بأسطر المصدر؛ مجموعها 726 سطراً | OBSERVED اليوم | `ls -1 work/msg-ext-*.md | wc -l` = 8؛ `cat work/msg-ext-*.md | wc -l` = 726. تناقض: handoff/MEMORY.md كان يقول 815 — **حُسم** بقياس 2026-11-10 (`wc -l work/msg-ext-*.md` = 726 بتوزيع 79/116/56/107/78/114/87/89) وصُحِّحت MEMORY.md [OBSERVED 2026-11-10] |
| عتبات غير مملأة | repo/config/thresholds.yaml سطرا 9–14 = 6 قيم null: top_k وrecall_at_k وrecall_target وanswer_latency_max_s وrerank_latency_max_s وfaithfulness_min | OBSERVED اليوم | `grep -n 'null' repo/config/thresholds.yaml` = 6 |
| نتائج BM25 هيثم | 12/15 أولى، 14/15 أول 3 (210 صفحة)، عناوين 8/8، صياغات 1/3 (28 و35) | REPORTED | work/analysis-wiki-talk-01.md §1.10 |
| الرام لحظة القياس الأصلي | 429MB — تضمين 1–2GB غير ممكن، مؤجل | REPORTED | work/analysis-wiki-talk-01.md §1.10 |

> أرقام wikillm (27,742/5) وأرقام Infinite Brain (584/228) منقولة من تقارير نموذج آخر ولم تُفتح نظيراتها على القرص هنا — تبقى REPORTED بمصدرها. أي رقم رخيص القياس نقيسه بنفسك قبل بنيته. [REPORTED — تنبيه repo/CONTEXT.md §3]

## 4) المتعارضات المفتوحة — لا يحسمها إلا المستخدم، كلها UNKNOWN / awaiting-user

> لا تنفَّذ أي مهمة مرتبطة بها قبل رد صريح من المستخدم. [REPORTED — work/plan-cycle-02.md §5 + قاعدة البريف «التعارضات التي لا يحسمها إلا المستخدم»]

| # | التناقض والوجهان | مصدر |
|---|---|---|
| D1 | الحجر الصحي مقابل عرض الطرفين: إبعاد الصفحة المتناقضة من الاسترجاع لحكم إنسان (وقد يُقصر الحجر على التناقض الميكانيكي رقم/تاريخ)، مقابل «مفيش حجر خالص، ونعرض الطرفين دايماً». | repo/docs/CONTRADICTION-POLICY.md + work/plan-cycle-02.md §5-D1 + البريف سطرا 3 و84–87 |
| D2 | حدّ «الرأي الغبي جداً / خارج المجال»: الاستثناء الوحيد الكامل في قاعدة المحتوى، ولا يوجد تعريف له — وصفه البريف نفسه بـ«أخطر قرار غير محسوم». البدائل: تعريف دلالي / لائحة أمثلة / لجنة بشرية لكل حالة. | البريف سطرا 34–35 و239 + repo/docs/RULES.md القاعدة 2 |
| D3 | قيمة k (Top-k): لا قيمة معلنة في البريف، وملف العتبات كله null؛ تُملأ بعد أول قياسين فقط، لا قبلها برقم مخترع. | البريف سطر 74 + repo/config/thresholds.yaml:9-14 (OBSERVED اليوم) |
| D4 | خاص مقابل عام: البريف حرفياً «مفيش نشر، المستودع خاص» (سطر 11)، وrepo-plan-01.md §1.2.1 يفرضه؛ لكن سؤال «النشر العام هدف أم وسيلة؟» مسجل مفتوحاً. كل تغيير يحتاج إذنا صريحاً. | البريف سطر 11 + work/repo-plan-01.md §1.2.1 + repo/CONTEXT.md §6 |
| D5 | تدوير PAT: القيمة معتمة في الملفات، وحالة الإبطال على الخادم UNKNOWN — المستخدم وحده يدوّر. تفصيلها §6. | work/secrets-2ndpass-2026-11-07.md §4 |
| D6 | إطلاق الدورة 2 (مهام T1–T10 وفحوص K1–K12): الآن، أو بعد D1–D5، أو إلغاء الدورات 2–4. | work/plan-cycle-02.md §5-D6 |
| D7 | «خلى glm يشتغل مكانك» مقابل «اشتغل انت حاليا» — تناقض حرفي داخل «كلام الويكي»: رسالة 48 (2026-10-30 21:31): «ومش تشتغل بنفسك خلى glm يشتغل مكانك واحفظ مفتاح api عندك». رسالة 59 (2026-10-31 20:59): «شغل ايجنتس تكون شغالة ب glm 5.3 حصرا مش تشتغل بنفسك». ثم رسالة 62 (2026-10-31 21:05): «وglm ضيفه في اوبن كود واشتغل انت حاليا». ورد Muse في 63: «تمام، اشتغلت أنا دلوقتي» — وقال فيها أيضاً إن مسار وكلاء glm لم يكتمل (ينقص مفتاح Yukino لحظياً وإعادة تشغيل سيرفر الترمنال، و«مش هدعي إن وكلاء glm شغالين»). أي قاعدة تُعتمد للجلسة: وكلاء فرعيون عموماً (AGENTS.md الحالي بلا شرط موديل)، أم وكلاء glm حصراً (48/59)، أم عمل مباشر عند الحاجة (62)? | source-transfers/wiki_all_talk.md أسطر 1172–1175 و1282–1285 و1317–1320 (OBSERVED اليوم بقراءة sed) + handoff/conversation-export.md (رسالة 63) |

## 5) أين كل شيء — خريطة الصندوق

- `/workspace/promptastra6fgss.md`: البريف الأصلي، 275 سطراً / 33,456 بايت. [OBSERVED — قراءة كاملة + `ls -la /workspace/*.md`]
- `/workspace/transfernow-download/`: `prompt.md` (233 سطراً — البرومبت الفيديوي، خارج النطاق) + ملف صوتي PTT-20261103-WA0000.opus. [OBSERVED وجوده اليوم / REPORTED 233 سطراً — work/repo-plan-01.md §1.2]
- `/workspace/layered-wiki-rag-design.md`: التصميم الكامل 94,124 بايت، مرجع ARCHITECTURE. [OBSERVED اليوم]
- `/workspace/layered-wiki-rag-guide.html`: نسخة HTML 131,743 بايت. [OBSERVED اليوم]
- `/workspace/wiki/`: جذر الصندوق. 14 ملفاً على الجذر (منها الأرشيف المضغوط + .env.example + .gitignore + 11 ملفاً .md مرآة) و13 مجلداً. [OBSERVED اليوم — `ls`]
- `/workspace/wiki/repo/`: **النسخة المعتمدة لمزامنة GitHub**، 42 ملفاً، بلا .git محلياً. الشجرة الكاملة في repo/docs/STRUCTURE.md. [OBSERVED — `test -d repo/.git` غائب]
- داخل repo: config/ (شخصيات وكتب ونماذج وعتبات)، docs/ (11 ملفاً منها GOALS وRULES وSTRUCTURE وEVALUATION وCONTRADICTION-POLICY)، sources/ (5 فهارس)، index/ (2)، masters/ (2)، reference/ (2)، templates/ (2)، timeline/ (1). [OBSERVED — أسماء من `find repo -type f`]
- `/workspace/wiki/work/`: 62 ملفاً = 33 سجل مخفي .log-* (أدلة تنفيذ خام، ممنوع نشرها؛ أشهرها .log-push و.log-review4 بـ1,493 سطراً و.log-session-c بـ3,051 و.log-archive بـ295) + 29 ملفاً ظاهراً: تحليلات (analysis-session-01، analysis-wiki-talk-01، archive-inventory-01، archive-report-extract-01، history-2026-11-06، msg-anchor-index)، خطتا repo-plan-01 وplan-cycle-02، مراجعات review-1..4 مع review-1-partA/B/C وreview-3-verify، secrets-2ndpass-2026-11-07، upload-report، research-01، msg-ext-01..08، remote-tree-2026-11-05.json و-06.json. [OBSERVED اليوم — `ls -la work/`]؛ تحديث 2026-11-10: أصبحت **63 = 33 + 30** (27 md سابقاً ثم 28 بظهور `security-fix-2026-11-10.md`، ملف جديد على القرص غير من إنتاج وكيل هذا الملف) [OBSERVED — `find work -maxdepth 1 -type f | wc -l` = 63 و`: -name '.log-*'` = 33 و`: ! -name '.log-*'` = 30]
- `/workspace/wiki/archive-extract/`: استخراج الأرشيف، جذر وحيد WIKI_ARCHIVE_2026-11-03، فيه 2,685 ملفاً / 211M. **مستبعد من النظافة، يُعدّ فقط ولا يُفتح** (تفصيله §6). [OBSERVED اليوم والعدد / REPORTED لهيكل 00_INDEXES…07_ENRICHMENT]
- `/workspace/wiki/WIKI_ARCHIVE_2026-11-03.tar.gz`: 60,072,453 بايت، 3,664 مدخلاً، sha256 في §3. نسخة مطابقة في source-transfers/github-release/. [OBSERVED اليوم]
- `/workspace/wiki/source-transfers/`: wiki_all_talk.md (175,533B / 2,012 سطراً / 106 رسالة) + 3 تنزيلات TransferNow: 202611035dwLrJSx/ (فيه prompt.md الفيديوي + opus)، 20261103BdZVc6uf/ (فيه pro.md تعليمات الجلسة)، 20261103UuphJtM8/ (فيه «ملف كل كلام الوكي.md») + UuphJtM8.html (100,618B) + github-release/ (فيه layered-wiki-rag-v1.0.0.tar.gz بحجم 77,980B + repo-tree.json لشجرة السجل الأول 5b70e59 — يساعد على فحص فجوة 404 محلياً). [OBSERVED اليوم — `ls` و`head`]
- `/workspace/wiki/handoff/`: ملفات التسليم، لا تُرفع قبل مراجعة بشرية. اليوم (2026-11-10): `README.md` و`CONTEXT.md` و`MEMORY.md` و`WHAT-WAS-DONE.md` (26,035 بايتاً) و`HANDOFF.md` (8,170 بايتاً، sha256 يبدأ `c2822e4a`) و`REVIEW-PREUPLOAD.md` (28,323 بايتاً) و`_pkg/` (فيه `PACKAGE-LOG.md` 30,106 بايتاً و`EXCLUDE-LIST.txt` 1,598 بايتاً — قياس 2026-11-10؛ PACKAGE-LOG كان 23,645 في 2026-11-09) و`conversation-export.md` (342,272 بايتاً) و`conversation-export.json` (1,709,609 بايتاً قياس 2026-11-10 — كان 1,709,588 في 2026-11-09 وتغير لحظياً 09:06)؛ مراجع `ls handoff` = 8 ملفات + `_pkg/`. قائمة 2026-11-09 القديمة (5 ملفات بأحجامها من ضمنها README.md بـ9,502B و«الغيابان» WHAT-WAS-DONE وHANDOFF) متجاوزة بالكامل — راجع فهرس README §(b) للأحجام الحية. [OBSERVED اليوم — `ls -la handoff/` 2026-11-10 + `wc -c` + `sha256sum handoff/HANDOFF.md`]
- مرآة الجذر /workspace/wiki/*.md (11 ملفاً): نسخ من محتوى repo على جذر الصندوق، لكنها ليست الكلمة الواحدة: روابطها تكتب work/… بينما repo يكتب ../work/… (كلاهما يشير فعلياً إلى /workspace/wiki/work/). مثال مقاس: CONTEXT.md في الجذر 16,914 بايت وفي repo 17,160 بايت على 116 سطراً للاثنين، وMESSAGES.md متطابقة بالبتات. اعتمد repo/ هو المصدر. [OBSERVED اليوم — `cmp` و`diff` و`wc -c`]

## 6) الوضع الأمني — قواعد حديدية

- التاريخ: مفتاح GitHub شخصي ظهر قيمةً في ملفات عمل سابقة، وموضعاه الموثقان: `.log-analysis-session-b` (موضع واحد، السطر 74) و`.log-session-c` (خمسة مواضع، الأسطر 71 و807 و915 و935 و967). [REPORTED — work/analysis-session-01.md §4–§5 + work/secrets-2ndpass-2026-11-07.md §3 + work/repo-plan-01.md §تحديث 2026-11-06]
- حالة الحجب اليوم: 6/6 المواضع معتمة بالبديل `[REDACTED-PAT-40chars-ROTATE-REQUIRED]`. ملاحظة: work/repo-plan-01.md وwork/secrets-2ndpass-2026-11-07.md ذكرا نص البديل في سرد العملية، وليسا موضعين للقيمة نفسها. [OBSERVED اليوم — `grep -rFlc 'REDACTED-PAT-40chars-ROTATE-REQUIRED' work/` (ظهر في 4 ملفات: السجلان + الملفان النصيان) + secrets-2ndpass §3]
- إبطال/تدوير المفتاح على خادم GitHub = UNKNOWN. التعطيل في الملفات لا يعني إبطال المفتاح. المستخدم وحده يدوّر يدوياً من GitHub → Settings → Developer settings → Personal access tokens، حتى لو بدت الفحوصات نظيفة. ولا يُدوَّر أي مفتاح من داخل بيئة وكيل (لا شبكة ولا صلاحية). [UNKNOWN — secrets-2ndpass §4 + handoff/README.md §(e)1]
- ممنوع طباعة أي قيمة سرية إطلاقاً: لا في أمر ولا URL ولا تقرير ولا رد. عند إظهار نتائج فحص: file:line + أول 8 محارف من المطابقة كحد أقصى. [REPORTED — secrets-2ndpass §1 + repo-plan-01.md §1.2.4]
- archive-extract/ إرث أسرار معروف: 2,947 مطابقة قوية في 54 ملفاً (أنماط مفاتيح وكوكيز قديمة داخل المحادثات الخام). اجري **عدّاً فقط**، ولا تُفتح ولا تُطبع محارفها من أي فحص هنا. مواضعها مستبعدة من النطاق النظيف، و`.gitignore` في repo يستثنئها حرفياً مع source-transfers/ و*.tar.gz. [REPORTED — secrets-2ndpass §1؛ ووسم .gitignore نفسه OBSERVED اليوم]
- نظافة repo: صفر مطابقة قوية (أنماط ghp_/github_pat_/sk-/AKIA/xox/Bearer/AIza) في repo وwork وconfig وdocs وsources وindex وmasters وtemplates وreference وtimeline وجذر *.md في جولة 2026-11-07. بقي فحص إعادة المسح الشامل بعد آخر رفعه: NOT_RUN. [REPORTED — secrets-2ndpass §1 و§4 + خطة `repo-plan-01.md` §5.2]
- .env.example بقيمة فارغة فقط: سطر واحد `YUKINO_API_KEY=` بلا قيمة (16 بايت). مفتاح Yukino يُستخدم لحظياً من متغير بيئة ولا يُكتب نصاً أبداً. [OBSERVED اليوم — `cat repo/.env.example`]
- .gitignore في repo مصفّح أمنياً 2026-11-05: يمنع *.env مع *!.env.example، و.hcnsec_key، وcookies.txt، و*.db، وMANIFEST.json، وzcode-*، وarchive-extract/، وsource-transfers/، و*.tar.gz و*.tgz و*.gz و*.csv و.patterns سجلات .log-*. راجعه قبل كل commit. [OBSERVED اليوم — `head repo/.gitignore`؛ والتاريخ REPORTED من repo-plan-01.md §تحديث 2026-11-06]
- هناك ملفات حساسة محلية خارج repo في /workspace: سجلات zcode-* وcloudflared وملف zcode-web-token.txt وغيرها — لا تُرفع ولا تُطبع ولا يتلمسها وكيل إطلاقاً. [REPORTED — أسماءها في ممنوعات work/repo-plan-01.md §1.2.4؛ ووجودها في الجذر OBSERVED اليوم بـ`ls /workspace` دون فتح أي محتوى]

## 7) البيئة والتشغيل

- لا يوجد .git محلي في repo/: النسخة المحلية تعمل كمرآة يدوية، والنسخة البعيدة أغنى منها (60 ملفاً مقابل 42، فارق 18 ملفاً). أول خطوة ترحيل: استنساخ المستودع على الجهاز الجديد، ثم فحص العدادات 42/57/2,713 كما في handoff/README.md §(d). [OBSERVED غياب .git اليوم] [REPORTED فرق 18 — work/upload-report.md]
- قاعدة الموجات: موجة 10 انهارت بحد الاستخدام المجاني، وموجتا 4 و6 انهارا بعطل مزوّد، ثم وكيل اختبار واحد نجح بعدها. المرجع المكتوب في handoff/MEMORY.md §4.1: «5–6 وكلاء لكل موجة» موسوم PROPOSED. الدليل الفعلي الموجود على القرص: موجة 8 (msg-ext) اكتملت. القاعدة العملية: موجات صغيرة متتابعة فقط، لا موجة عشر دفعة واحدة. [REPORTED — handoff/conversation-export.md حوالي السطر 3173]
- أدوات YAML غائبة محلياً: python3 بلا وحدة yaml وruby غير مثبت، فتحقق repo/config/*.yaml يبقى NOT_RUN (المهمة T4 والفحص K5). [REPORTED — work/plan-cycle-02.md §2]
- لا شبكة في جلسة الكتابة هذه: كل قياس هنا من القرص المحلي فقط، ولا أي عملية شبكية في هذا الملف. [OBSERVED — قيود جلسة الكتابة]

## 8) ما ليس منجزاً الآن

- ما وعده handoff/README.md §(b) بعنوان «سوف يُكتب»: WHAT-WAS-DONE.md وHANDOFF.md؛ **كلاهما موجود الآن** (`ls handoff` = 8 ملفات + `_pkg/`) — أقرأهما قبل الاعتماد. [OBSERVED 2026-11-10 — `ls -la handoff/`]؛ سابقاً غائبان في 2026-11-09. [OBSERVED]
- تناقضان سجليان: (1) msg-ext = 726 سطراً مقابل 815 في MEMORY.md — **حُسم**: قياس 2026-11-10 `wc -l work/msg-ext-*.md` = 726 وصُحِّحت MEMORY.md [OBSERVED 2026-11-10]؛ (2) الاستخراج المحلي = 2,685 ملفاً مقابل 2,713 في الجرد — **باقٍ غير محسوم** (أُعيد القياس 2026-11-10: `find archive-extract -type f | wc -l` = 2,685). [OBSERVED 2026-11-10 / REPORTED قيمة الجرد]
- MESSAGES.md فيها 57 من 106 صفّاً (فجوة 49)، وهي المهمة T1/G1 في plan-cycle-02، وكل ما يخصها مؤجل على إطلاق الدورة 2 (D6) وقرار المستخدم. [REPORTED — work/plan-cycle-02.md §1]
- ما بعد الرفع كلّه NOT_RUN: إعادة فحص الأسرار بعد الدفع، وتحقق YAML، وفحص الروابط (T3 وT4 وT5 مع K3 وK5 وK6). [REPORTED — work/plan-cycle-02.md §4]

## 9) حدود هذا الملف

- أرقام هذا الملف قابلة للتغيير على الحاسوب الجديد: قِسها قبل الاعتماد، واعتمد القياس الجديد المُسجَّل لا الكلام القديم. [PROPOSED]
- هذا الملف لا يستبدل AGENTS.md ولا RULES/GOALS ولا خطتُي repo-plan-01 وplan-cycle-02. [PROPOSED]
- ما لم تجده في هذا الملف لا تخترعه: وسّمه UNKNOWN مع مصدر صريح. [PROPOSED]

---

> **سجل الكتابة:** كتبه وكيل فرعي بتاريخ 2026-11-09 من بيئة بلا شبكة ولا git محلي. كل رقم فيه إما مقاس بأمر مذكور، أو منقول موسوم بمصدره، أو مفقود موسوم UNKNOWN/NOT_RUN.
> **سجل تصحيح 2026-11-10:** وكيل فرعي مصحِّح (مهمة تنقيح مراجعة ما قبل الرفع) أصلح: إخفاءات JSON (75 بالأمر المدوَّن)، حسم تناقض msg-ext (815/726 وصُحِّحت MEMORY.md)، حصر handoff اليوم (8 ملفات + `_pkg/` بعد أن كان الغيابان WHAT-WAS-DONE/HANDOFF)، وتحديث قسمة work إلى 33+30=63 بملف جديد ظاهر — الأمر مؤرَّخ داخل كل خلية صُحِّحت. [OBSERVED]
> **أول فحص عند الاستقبال:** أعد قياس عدادات §3. إن اختلفت أي قيمة من 42/57/2,713، توقف ووثّق الفارق قبل أي تعديل، كما يوجب handoff/README.md §(d).
