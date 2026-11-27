# N318: 多重比较校正对p-value阈值的调整：若同时检验K个假设（如K=5个品类或K=3个时间尺度），需使用Bonferroni校正，显著性水平调整为 α_adj =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

多重比较校正对p-value阈值的调整：若同时检验K个假设（如K=5个品类或K=3个时间尺度），需使用Bonferroni校正，显著性水平调整为 α_adj = 0.05/K。例如K=5时，p-value需<0.01才视为显著。该修正直接改变'置信度为高'的判定边界，需将原始p-value与α_adj对比而非0.05。

## Corrected Claim

多重比较校正对p-value阈值的调整：若同时检验K个假设（如K=5个品类或K=3个时间尺度），需使用Bonferroni校正，显著性水平调整为 α_adj = 0.05/K。例如K=5时，p-value需<0.01才视为显著。该修正直接改变'置信度为高'的判定边界，需将原始p-value与α_adj对比而非0.05。

## Evidence

先验知识/题面给定，逻辑校验通过：Bonferroni校正公式 α_adj = α/K 是统计学标准定义，K=5时 0.05/5=0.01 计算正确，逻辑自洽。
