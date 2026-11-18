# N256: FP8 量化相对于 BF16 的质量损失可接受性判断标准：如果 MMLU 准确率下降 < 0.5% 且 Perplexity 增加 < 0.1，则视为可接受。Q

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

FP8 量化相对于 BF16 的质量损失可接受性判断标准：如果 MMLU 准确率下降 < 0.5% 且 Perplexity 增加 < 0.1，则视为可接受。Qwen3-27B FP8 量化通常满足此标准，因此推荐在显存受限场景下使用 FP8

## Corrected Claim

FP8 量化相对于 BF16 的质量损失可接受性判断标准：如果 MMLU 准确率下降 < 0.5% 且 Perplexity 增加 < 0.1，则视为可接受。Qwen3-27B FP8 量化通常满足此标准，因此推荐在显存受限场景下使用 FP8

## Evidence

先验知识/题面给定，逻辑校验通过
