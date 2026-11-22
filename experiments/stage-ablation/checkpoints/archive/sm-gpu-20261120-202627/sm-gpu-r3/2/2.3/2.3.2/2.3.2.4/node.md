# N225: Qwen3-27B 在 GSM8K 数据集上 AWQ-INT8 量化后的准确率 (Accuracy_AWQ)，用于计算相对 BF16 基线的绝对下降值，验证是否

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56, N57, N58

## Claim

Qwen3-27B 在 GSM8K 数据集上 AWQ-INT8 量化后的准确率 (Accuracy_AWQ)，用于计算相对 BF16 基线的绝对下降值，验证是否小于 1%

## Corrected Claim

Qwen3-27B 在 GSM8K 数据集上 AWQ-INT8 量化后的准确率相对 BF16 基线的下降幅度需通过实际基准测试验证，通常预期较小，但具体是否小于 1% 缺乏当前来源支持。

## Evidence

[质询]该陈述包含具体的经验性数值结论（准确率下降小于1%），属于硬件/模型性能指标，无法从第一性原理推导，且当前无可用来源支持该具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B AWQ INT8 GSM8K accuracy evaluation
