# تقرير التحقق من ملفات YAML — 2026-11-11

**النطاق:** `/workspace/wiki/repo/config/*.yaml` + `/workspace/wiki/config/*.yaml`
**القيود:** قراءة فقط على ملفات التهيئة (لم يُعدَّل أي ملف تهيئة) · بلا شبكة · أوامر صغيرة مفردة · لم يُطبع أي سر.
**الدور:** وكيل فرعي للتحقق — المخرج الوحيد: هذا الملف.

---

## 1) الجرد والأحجام

`OBSERVED` — الأمر: `ls -la` + `wc -lc`:

| الملف (repo/config) | الأسطر | البايت | في /workspace/wiki/config |
|---|---|---|---|
| books.yaml | 25 | 1395 | موجود |
| models.yaml | 42 | 1953 | موجود |
| personas.yaml | 54 | 2545 | موجود |
| thresholds.yaml | 21 | 939 | موجود |

المجموع: 4 ملفات، 284 سطر، 13664 بايت في كل مجلد.

---

## 2) الصلاة النحوية

- `OBSERVED` — `python3 --version` → Python 3.13.5 متوفر.
- `OBSERVED` — `python3 -c "import yaml"` → `ModuleNotFoundError: No module named 'yaml'` — **pyyaml غير مثبت**.
- `NOT_RUN` — التثبيت عبر pip مرفوض (شبكة ممنوعة). فحصت بدائل محلية: `which yq yq-go ruby perl` → لا yq ولا ruby؛ `perl -MYAML` → `BEGIN failed--compilation aborted` (وحدة YAML غير موجودة).
- **النتيجة: التحليل الرسمي بمحلل YAML حقيقي = NOT_RUN** (لا محلل متاح محلياً ولا شبكة). الفحص البنيوي البديل:
  - `OBSERVED` — `grep -Pn '\t'` على الملفات الأربعة → **صفر Tab** (خروج 1 = لا تطابق). Tab غير صالح في مسافة YAML البادئة.
  - `OBSERVED` — `awk` لعدّ المسافة البادئة لكل سطر: أنماط متسقة في كل الملفات (زيادات 2):
    - books.yaml: 0→2→4→6 (L7 sources / L8 slug / L9 books / L10,17-20 `- title_ar`) — بنود القائمة مسبوقة بـ `-` أي بنود منفصلة **وليست** مفاتيح مكررة.
    - models.yaml: 0→2→4 متسق (L10/L11/L12…).
    - personas.yaml: 0→2→4 متسق (L11/L12/L13…).
    - thresholds.yaml: مفاتيح جذر 0 (L5,6,8,16,21) وتفرعات 2 (L9-14, L17-19) — متسق.
  - `OBSERVED` — بنود `title_ar` في books.yaml L10 وL17-L20 كلها ببادئة `- ` → بنود قائمة مستقلة (لا خطر مفاتيح مكررة في نفس الخريطة).
- `PROPOSED` — بناءً على الفحص البنيوي فقط: لا توجد موانع بنوية واضحة، لكن هذا **لا يعادل** صلاة YAML رسمية.

---

## 3) مراجعة المحتوى لكل ملف

### books.yaml — لا مشاكل
- `OBSERVED` — المفاتيح: `sources` (3 بنود slug: ibn-sirin / ibn-taymiyyah / ibn-al-qayyim) + `notes` (3 بنود statement).
- `OBSERVED` — ibn-taymiyyah `books: []` (L13) مع مبرر نصي في L23: المصدر §1.5 لم يذكر كتباً له — انضباط بوسم المصدر.
- `OBSERVED` — المخطط مطابق لـ `work/repo-plan-01.md` L85 (قوائم كتب يُعاد من yt-wiki) والمصادر موثقة في التعليقات (analysis-wiki-talk-01.md §1.4/§1.5).
- `OBSERVED` — slugs الثلاثة جميعها موجودة في personas.yaml (اتساق داخلي).

### models.yaml — لا مشاكل
- `OBSERVED` — المفاتيح: `selection_status: "NOT_RUN"` (L6)، `chosen_embedding_model: null` (L7)، `chosen_chat_model: null` (L8)، `embedding_candidates` (3 بنود)، `chat_candidates` (1)، `vector_stores` (2)، `blocked_rule` (L42).
- `OBSERVED` — كل المرشحين `status: "conditional-on-test"` — لا اختيار نهائي، مطابق لقاعدة «لا تضمين قبل اختباره» (analysis-wiki-talk-01.md L181).
- `OBSERVED` — محتوى المرشحين مطابق حرفياً لجدول المصدر (analysis L376-379): bge-m3 بـ **1024 بُعد** ✓، e5-large «الرسالة 44» ✓، FastEmbed «الرسالة 46» ✓، glm-5.3-free/Yukino «المفتاح لحظياً + إعادة تشغيل الترمنال» ✓.
- `OBSERVED` — المخطط مطابق لـ repo-plan-01.md L86 (مرشحون مشروطون، لا اختيار مفروض).

### personas.yaml — مشكلة واحدة (مصدرية)
- `OBSERVED` — المفاتيح: `total_observed_pages` (L7)، `total_observed_bytes` (L8)، `total_evidence` (L9)، `personas` (6 بنود بـ slug/name_ar/domain/domain_evidence/observed_pages/notes).
- `OBSERVED` — الأعداد مطابقة حرفياً لـ `repo/CONTEXT.md` L21: 780 / 81 / 556 / 210 / 1423 / 2846 ✓، والمجاميع لـ L20: 5896 صفحة و31262266 بايت ✓ (مطابقة أيضاً `repo/README.md` L44).
- `OBSERVED` (حساب) — `python3 -c` → مجموع observed_pages = **5896** = total_observed_pages ✓ اتساق داخلي.
- `OBSERVED` — ibn-taymiyyah وibn-al-qayyim: `domain: "UNKNOWN"` + `domain_evidence: "UNKNOWN"` (L21-22، L28-29) مع ملاحظة «لا تُخترع مجالا» — التزام بوسوم الأدلة.
- ⚠️ **المشكلة 1:** L38 `observed_bytes: 601084` وL39 `avg_page_bytes: 2336` — والحساب 601084÷210 = **2862.3** لا 2336. القيمتان كلتاهما منسوختان بأمانة من مصدرين مختلفين في `repo/CONTEXT.md` (L25: «كامل 210 صفحة… 601084 بايت» من §1.10، مقابل L23: «متوسط صفحة هيثم 2336 بايت» من §1.7) — أي أن التعارض **موجود في المصدر نفسه** ولم يُصنع في التهيئة، لكنه تعارض حسابي غير محسوم داخل نفس الملف. `UNKNOWN` سبب الفرق (وسيط مختلف؟ عيّنة مختلفة؟). إضافياً: `avg_page_bytes` بلا وسام دليل مباشر على السطر (بقية الأرقام مسنودة عبر total_evidence/الملاحظات).

### thresholds.yaml — لا مشاكل
- `OBSERVED` — `status: "NOT_RUN"` (L5) + note صريح «لا تُملأ من التخمين» (L6).
- `OBSERVED` — **قيم k والقيم القياسية كلها null** كما هو مطلوب:
  - L9 `top_k: null`
  - L10 `recall_at_k: null`
  - L11 `recall_target: null`
  - L12 `answer_latency_max_s: null`
  - L13 `rerank_latency_max_s: null`
  - L14 `faithfulness_min: null`
- `OBSERVED` — متسق مع الوثائق: `repo/docs/EVALUATION.md` L38 و`repo/docs/GOALS.md` L43: «قيمة k والعتبة: UNKNOWN — لا قيمة k معلنة في البريف (مقترح k=10 — القيمة النهائية UNKNOWN، config/thresholds.yaml)» — أي أن الملف ترك k فارغاً بدل تعبئته بالقيمة المقترحة 10، وهذا هو السلوك الصحيح حسب fill_rule (L21): «يُوسم أي اقتراح قبله PROPOSED لا OBSERVED».
- `OBSERVED` — `todo` (L16-19) و`fill_rule` (L21) مطابقان لـ `repo/ARCHITECTURE.md` L81: «العتبات تصبح في config/thresholds.yaml يوم أول قياسين؛ لا رقم مخترع قبلها».
- `OBSERVED` — المخطط مطابق لـ repo-plan-01.md L87 (عتبات k/Recall/زمن تُملأ بعد أول قياسين).
- ملاحظة نطاق: «الرأي الغبي/المختلف» حدودُه موثقة UNKNOWN في `repo/docs/RULES.md` L10 و`CONTRADICTION-POLICY.md` L16 و`CHUNKING.md` L25 و`ARCHITECTURE.md` L98 — لكن مخطط repo-plan-01.md §2 يعرّف thresholds.yaml بعتبات k/Recall/زمن فقط، فغياب هذا المفتاح **ليس خللاً** في الملف (خارج نطاق مخططه).

---

## 4) الاتساق بين المجلدين

- `OBSERVED` — `diff -rq /workspace/wiki/repo/config /workspace/wiki/config` → **لا خرج نهائياً وخروج 0** = المجلدان متطابقان بايت-ببايت في الملفات الأربعة. لا نسخة قديمة ولا انزياح بينهما.

---

## 5) الأسرار

- `OBSERVED` — `grep -c -i "password|passwd|token|api_key|apikey|secret|Bearer|sk-|ghp_|BEGIN.*PRIVATE"` (عدّاد فقط، دون طباعة محتوى) → **0 تطابق في الملفات الثمانية**. لا أسرار، متسق مع تعليق «لا أسرار في هذا الملف» في books.yaml L5 وpersonas.yaml L5.

---

## 6) جدول الحكم

| الملف | صلاة نحوية | المفاتيح سليمة | متسق مع repo/docs | عدد المشاكل |
|---|---|---|---|---|
| books.yaml | بنيوي ✓ / تحليل رسمي NOT_RUN | ✓ (sources+notes مطابق للمخطط §2) | ✓ (analysis §1.4/§1.5؛ slugs ⊂ personas) | 0 |
| models.yaml | بنيوي ✓ / تحليل رسمي NOT_RUN | ✓ (لا اختيار نهائي؛ كل شيء conditional) | ✓ (analysis L376-379 حرفياً؛ القاعدة L181) | 0 |
| personas.yaml | بنيوي ✓ / تحليل رسمي NOT_RUN | ✓ (6 شخصيات؛ المجموع الداخلي 5896 ✓) | ✓ (CONTEXT L20-23؛ عدًا مشكلة 1) | 1 |
| thresholds.yaml | بنيوي ✓ / تحليل رسمي NOT_RUN | ✓ (كل العتبات null؛ NOT_RUN؛ todo+fill_rule) | ✓ (EVALUATION L38؛ GOALS L43؛ ARCHITECTURE L81) | 0 |

**إجمالي المشاكل: 1** (personas.yaml L38/L39: تعارض حسابي مصدري بين 601084÷210=2862.3 وavg=2336 — منسوخ بأمانة من مصدرين مختلفين، سببُه UNKNOWN).

## 7) الحدود والصدق

- لم يُعدَّل أي ملف تهيئة (قراءة فقط) — `OBSERVED`.
- لم يُشغَّل محلل YAML رسمي (لا pyyaml/لا yq/لا ruby/لا وحدة Perl، والشبكة ممنوعة) — `NOT_RUN`؛ حكم الصلاة النحوية قائم على الفحص البنيوي فقط (tabs + اتساق المسافة البادئة) — `PROPOSED` وليس `OBSERVED` كصلاة كاملة.
- لم يُجرَّب التحقق التشغيلي (تحميل الملفات في تطبيق فعلي) — `NOT_RUN`.
- لا شبكة، لا أسرار مطبوعة — `OBSERVED`.
