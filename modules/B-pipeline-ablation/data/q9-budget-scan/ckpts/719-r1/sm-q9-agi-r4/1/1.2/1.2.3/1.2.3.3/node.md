# N131: 逻辑连贯性错误的判定标准量化：使用 GPT-4o 作为裁判模型，对每 512 token 的滑动窗口进行二元分类（连贯/不连贯），当 FP8 窗口不连贯率比 F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

逻辑连贯性错误的判定标准量化：使用 GPT-4o 作为裁判模型，对每 512 token 的滑动窗口进行二元分类（连贯/不连贯），当 FP8 窗口不连贯率比 FP16 高超过 2 个标准差时记为一个 Coherence Error Event，以此构建 CER 数据集

## Corrected Claim

逻辑连贯性错误的判定标准量化：使用 GPT-4o 作为裁判模型，对每 512 token 的滑动窗口进行二元分类（连贯/不连贯），当 FP8 窗口不连贯率比 FP16 高超过 2 个标准差时记为一个 Coherence Error Event，以此构建 CER 数据集

## Evidence

先验知识/题面给定，逻辑校验通过
