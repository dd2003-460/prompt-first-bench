# N105: INT4 (AWQ) 量化在 MMLU 基准上的具体性能退化值：Qwen3-27B 在 BF16 下 MMLU 准确率为 [待核验: 需查 Qwen3 技术报告

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

INT4 (AWQ) 量化在 MMLU 基准上的具体性能退化值：Qwen3-27B 在 BF16 下 MMLU 准确率为 [待核验: 需查 Qwen3 技术报告]，INT4 AWQ 下通常下降 1.5-2.5 个百分点。若 BF16 基线为 75%，则 INT4 约为 72.5-73.5%。

## Corrected Claim

INT4 (AWQ) 量化在 MMLU 基准上通常会导致性能轻微下降，具体退化值需查阅 Qwen3 技术报告或相关基准测试数据。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU准确率基线及量化退化幅度），属于硬件/模型性能指标，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B MMLU benchmark INT4 AWQ accuracy vs BF16
