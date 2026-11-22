# N169: 业务可接受的质量损失阈值量化模型：Value_of_Quality_Loss = (P_error_increase * Impact_per_error) -

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N50, N51, N52

## Claim

业务可接受的质量损失阈值量化模型：Value_of_Quality_Loss = (P_error_increase * Impact_per_error) - (TCO_Saving * Discount_Factor)；其中 P_error_increase 需基于 MMLU 下降 1.5% 映射到实际任务错误率增加（如医疗/金融场景下错误率从 2% 升至 2.15%），Impact_per_error 为单次错误的平均业务损失（如 $500/次），需结合具体业务场景确定该阈值是否真正对应 1.5% MMLU 下降

## Corrected Claim

业务可接受的质量损失阈值量化模型框架：Value_of_Quality_Loss = (P_error_increase * Impact_per_error) - (TCO_Saving * Discount_Factor)；其中 P_error_increase 需基于基准测试（如 MMLU）下降幅度映射到实际任务错误率增加，Impact_per_error 为单次错误的平均业务损失，具体数值需结合特定业务场景（如医疗/金融）的实际数据进行校准，而非直接采用通用假设值。

## Evidence

[质询]该陈述包含具体的经验性数值假设（如医疗/金融场景错误率从2%升至2.15%、单次错误损失$500），这些属于特定业务场景下的经验事实，无法从第一性原理或数学公理中严格推导得出，且缺乏外部来源支持其具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持。公式结构在逻辑上合理，但具体的映射比例（1.5% MMLU -> 0.15% 错误率）和损失金额（$500）为假设值，无检索来源佐证。

## Search Query

MMLU score drop impact on real-world task error rate quantification business cost
