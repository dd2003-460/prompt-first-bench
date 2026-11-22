# N228: Qwen3-27B 在 MMLU 数据集上 INT8 量化（GPTQ 或 AWQ）后的总体准确率 (Accuracy_INT8)，用于计算相对 BF16 基线的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56, N57, N58

## Claim

Qwen3-27B 在 MMLU 数据集上 INT8 量化（GPTQ 或 AWQ）后的总体准确率 (Accuracy_INT8)，用于计算相对 BF16 基线的绝对下降值，验证是否落在 0.5%-1.5% 区间

## Corrected Claim

Qwen3-27B 在 MMLU 数据集上 INT8 量化（GPTQ 或 AWQ）后的总体准确率相对 BF16 基线的下降值通常较小，具体数值需查阅相关基准测试报告以确认是否落在 0.5%-1.5% 区间。

## Evidence

[质询]该陈述包含具体的经验性数值区间（0.5%-1.5%），属于硬件/模型性能经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B INT8 MMLU accuracy evaluation GPTQ AWQ
