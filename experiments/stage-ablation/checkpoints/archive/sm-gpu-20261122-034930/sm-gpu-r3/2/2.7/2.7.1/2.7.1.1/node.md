# N248: Qwen3-27B 在 W4 量化下，短文本 (1K 上下文) 的 Perplexity 增量 (相对于 BF16) 约为 0.3-0.5%，具体数值需基于 W

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86

## Claim

Qwen3-27B 在 W4 量化下，短文本 (1K 上下文) 的 Perplexity 增量 (相对于 BF16) 约为 0.3-0.5%，具体数值需基于 WikiText-103 或 C4 数据集的子集进行基准测试获取。

## Corrected Claim

Qwen3-27B 在 W4 量化下，短文本 (1K 上下文) 的 Perplexity 增量相对于 BF16 存在一定程度的增加，具体数值需基于 WikiText-103 或 C4 数据集的子集进行基准测试获取。

## Evidence

[质询]该陈述包含具体的经验性数值范围（0.3-0.5%），属于硬件/模型性能指标，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B W4 quantization Perplexity increment short context 1K
