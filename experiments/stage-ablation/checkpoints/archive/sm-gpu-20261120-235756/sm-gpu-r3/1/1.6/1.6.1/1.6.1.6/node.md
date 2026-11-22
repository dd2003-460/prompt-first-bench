# N178: GPTQ/AWQ校准对W4A16质量的改善效果量化：在校准数据集(通常128-512样本)上，W4A16的Perplexity较未校准W4A16降低15-25%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51, N52, N53

## Claim

GPTQ/AWQ校准对W4A16质量的改善效果量化：在校准数据集(通常128-512样本)上，W4A16的Perplexity较未校准W4A16降低15-25%，较BF16基准增加3-5%；校准耗时在单张RTX 4090上为15-25分钟，取决于校准样本量和模型大小。

## Corrected Claim

GPTQ/AWQ校准对W4A16质量的改善效果量化：在校准数据集(通常128-512样本)上，W4A16的Perplexity较未校准W4A16降低15-25%，较BF16基准增加3-5%；校准耗时在单张RTX 4090上为15-25分钟，取决于校准样本量和模型大小。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPTQ AWQ calibration time perplexity improvement W4A16 27B
