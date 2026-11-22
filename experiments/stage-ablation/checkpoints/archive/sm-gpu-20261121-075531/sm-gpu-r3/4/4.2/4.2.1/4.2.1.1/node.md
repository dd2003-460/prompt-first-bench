# N257: Qwen3-27B (BF16) 在 WikiText-2 数据集上的基线困惑度 (PPL) 精确值，作为计算 FP8 量化后 ΔPPL 的分母；若 BF16 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

Qwen3-27B (BF16) 在 WikiText-2 数据集上的基线困惑度 (PPL) 精确值，作为计算 FP8 量化后 ΔPPL 的分母；若 BF16 PPL 约为 6.5-6.8，则 FP8 上升至 6.8-7.3 意味着 ΔPPL 约为 0.3-0.5，需核实基线数值。

## Corrected Claim

Qwen3-27B (BF16) 在 WikiText-2 数据集上的基线困惑度 (PPL) 具体数值需查阅官方技术报告或基准测试数据；若基线 PPL 处于 6.5-6.8 区间，则 FP8 量化后 PPL 上升至 6.8-7.3 意味着 ΔPPL 约为 0.3-0.5。

## Evidence

[质询]该陈述包含具体的经验性数值（Qwen3-27B在WikiText-2上的BF16 PPL约为6.5-6.8），属于硬件/模型性能指标，无法从第一性原理推导，且检索无可用来源支持，存在数值偏差风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B WikiText-2 perplexity baseline BF16
