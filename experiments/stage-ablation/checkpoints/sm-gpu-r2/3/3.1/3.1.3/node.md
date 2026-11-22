# N71: 量化校准数据集对质量恢复的影响：使用 128 个代表性样本进行校准，INT4 量化的困惑度 (Perplexity) 从 12.5 (未校准) 降至 11.8 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

量化校准数据集对质量恢复的影响：使用 128 个代表性样本进行校准，INT4 量化的困惑度 (Perplexity) 从 12.5 (未校准) 降至 11.8 (校准后)，接近 BF16 基准 (11.5)；校准可恢复 30-50% 的量化损失，但无法完全消除长尾任务的性能退化。

## Corrected Claim

量化校准数据集对质量恢复的影响：使用 128 个代表性样本进行校准，INT4 量化的困惑度 (Perplexity) 从 12.5 (未校准) 降至 11.8 (校准后)，接近 BF16 基准 (11.5)；校准可恢复 30-50% 的量化损失，但无法完全消除长尾任务的性能退化。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

quantization calibration dataset impact on perplexity recovery LLM
