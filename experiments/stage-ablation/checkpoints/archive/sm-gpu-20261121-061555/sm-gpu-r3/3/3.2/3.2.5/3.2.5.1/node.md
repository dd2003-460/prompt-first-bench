# N245: NVFP4 量化下 Qwen3-27B 在 WikiText-2 或 C4 数据集上的 Perplexity (PPL) 具体数值及相对于 BF16 的增量，验

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

NVFP4 量化下 Qwen3-27B 在 WikiText-2 或 C4 数据集上的 Perplexity (PPL) 具体数值及相对于 BF16 的增量，验证是否控制在 <5% 质量损失阈值内，需确认是否使用微缩放因子（micro-scaling）补偿精度。

## Corrected Claim

NVFP4 量化下 Qwen3-27B 在 WikiText-2 或 C4 数据集上的 Perplexity (PPL) 具体数值及相对于 BF16 的增量需通过实验验证，目前缺乏公开数据确认其是否严格控制在 <5% 质量损失阈值内，以及是否使用微缩放因子补偿精度。

## Evidence

[质询]该陈述包含具体的经验性数值指标（PPL增量<5%）和特定技术实现细节（微缩放因子），属于硬件/模型性能经验事实，无法从第一性原理推导，且缺乏来源支持以确认具体数值和阈值是否准确。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

NVFP4 quantization Qwen3-27B perplexity loss vs BF16 H100 H200 benchmark
