# N114: 27B模型在小样本（n<30）下统计显著性误判的根源在于对p值阈值的语义理解偏差而非计算错误，其输出的p值与实际统计检验结果的Spearman相关系数仅为0.6

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

27B模型在小样本（n<30）下统计显著性误判的根源在于对p值阈值的语义理解偏差而非计算错误，其输出的p值与实际统计检验结果的Spearman相关系数仅为0.65，导致在真实p>0.05时错误报告显著性的概率（Type I Error inflation）达到25%。

## Corrected Claim

27B模型在小样本（n<30）下统计显著性误判的根源可能在于对p值阈值的语义理解偏差而非计算错误，其输出的p值与实际统计检验结果的相关性较低，导致在真实p>0.05时错误报告显著性的概率（Type I Error inflation）显著高于标准水平。

## Evidence

[质询]该陈述包含具体的经验性数值指标（Spearman相关系数0.65、Type I Error inflation 25%），这些并非从第一性原理或数学公理中严格推导出的必然结果，而是依赖于特定实验设置、数据集和评估方法的经验观测值。在没有具体文献支持的情况下，断言这些精确数值具有普适性或确定性缺乏依据。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且具体数值无法从第一性原理推出）

## Search Query

LLM statistical significance interpretation error small sample p-value calibration bias
