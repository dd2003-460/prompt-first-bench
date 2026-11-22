# N393: Qwen3-27B INT8 (AWQ) 量化在 WikiText-2 数据集上的困惑度 (PPL) 增量：相比 BF16 基线 (PPL ≈ 7.5-8.0)

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N125

## Claim

Qwen3-27B INT8 (AWQ) 量化在 WikiText-2 数据集上的困惑度 (PPL) 增量：相比 BF16 基线 (PPL ≈ 7.5-8.0)，INT8 量化后 PPL 通常增加 0.1-0.3 个绝对单位，即相对增加约 1.5%-4%。

## Corrected Claim

Qwen3-27B INT8 (AWQ) 量化在 WikiText-2 数据集上的困惑度 (PPL) 相比 BF16 基线通常会有轻微增加，具体数值需参考官方技术报告或基准测试数据。

## Evidence

[质询]该陈述包含具体的经验性数值（PPL基线7.5-8.0，增量0.1-0.3），属于硬件/模型性能指标，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B AWQ INT8 perplexity WikiText-2 benchmark
