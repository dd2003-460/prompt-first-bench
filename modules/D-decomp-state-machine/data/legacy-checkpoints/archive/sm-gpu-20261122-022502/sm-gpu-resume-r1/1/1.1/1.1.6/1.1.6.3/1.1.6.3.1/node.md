# N479: 在长上下文 (≥32K) 下，INT4 量化导致的 'Lost in the Middle' 现象加剧，MMLU-Pro 准确率相对于短上下文 (≤4K) 基准

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148

## Claim

在长上下文 (≥32K) 下，INT4 量化导致的 'Lost in the Middle' 现象加剧，MMLU-Pro 准确率相对于短上下文 (≤4K) 基准额外下降 1-2 个百分点 (例如从 72.5% 降至 70.5%-71.5%)。

## Corrected Claim

在长上下文 (≥32K) 下，INT4 量化导致的 'Lost in the Middle' 现象加剧，MMLU-Pro 准确率相对于短上下文 (≤4K) 基准额外下降 1-2 个百分点 (例如从 72.5% 降至 70.5%-71.5%)。

## Evidence

先验知识/题面给定，逻辑校验通过
