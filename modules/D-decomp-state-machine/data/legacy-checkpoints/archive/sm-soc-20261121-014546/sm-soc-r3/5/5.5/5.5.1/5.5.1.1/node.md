# N341: 锚点敏感度系数 β_anchor 的具体数值需通过回归模型 P_ask = α + β_anchor * P_display + ε 估计，其中 P_displ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N110

## Claim

锚点敏感度系数 β_anchor 的具体数值需通过回归模型 P_ask = α + β_anchor * P_display + ε 估计，其中 P_display 为平台展示的历史均价，需获取特定平台卖家挂价与展示价的配对数据以计算 β_anchor 的均值及 95% 置信区间。

## Corrected Claim

锚点敏感度系数 β_anchor 的估计通常涉及回归分析，具体数值需基于特定平台的历史交易数据通过统计模型（如 P_ask = α + β_anchor * P_display + ε）进行实证估计，并计算其均值及置信区间。

## Evidence

[质询]该陈述描述的是具体的实证研究方法论（回归模型设定及数据需求），属于经验事实范畴，无法从第一性原理或数学公理直接推导得出其具体数值或唯一正确的模型形式，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

seller price anchoring sensitivity coefficient regression beta anchor display price
