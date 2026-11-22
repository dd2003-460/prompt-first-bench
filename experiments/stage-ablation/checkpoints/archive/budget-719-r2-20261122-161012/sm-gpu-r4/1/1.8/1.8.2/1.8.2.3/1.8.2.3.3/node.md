# N463: 若业务约束为 GSM8K >= 90%，则 INT4 方案处于临界不可行区间（87-89% < 90%），必须升级至 INT8 或 FP8；而 FP8 方案（9

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191

## Claim

若业务约束为 GSM8K >= 90%，则 INT4 方案处于临界不可行区间（87-89% < 90%），必须升级至 INT8 或 FP8；而 FP8 方案（90.5-91.0%）满足约束，因此在该特定数学推理高敏场景下，FP8 是唯一同时满足精度与低比特压缩率的可行解。

## Corrected Claim

若业务约束为 GSM8K >= 90%，则 INT4 方案处于临界不可行区间（87-89% < 90%），必须升级至 INT8 或 FP8；而 FP8 方案（90.5-91.0%）满足约束，因此在该特定数学推理高敏场景下，FP8 是唯一同时满足精度与低比特压缩率的可行解。

## Evidence

先验知识/题面给定，逻辑校验通过：INT4精度(87-89%)低于阈值90%，FP8精度(90.5-91.0%)高于阈值90%，且FP8比特率低于INT8，符合'唯一同时满足精度与低比特压缩率'的逻辑推导。

## Search Query

LLM quantization GSM8K threshold 90% feasibility
