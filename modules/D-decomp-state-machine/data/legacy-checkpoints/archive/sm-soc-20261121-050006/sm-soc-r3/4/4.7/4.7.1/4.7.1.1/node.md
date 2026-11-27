# N282: 信息敏感度系数 α_info 的实证校准公式为：α_info = (ΔP_ask_treatment - ΔP_ask_control) / (P_ask_in

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89

## Claim

信息敏感度系数 α_info 的实证校准公式为：α_info = (ΔP_ask_treatment - ΔP_ask_control) / (P_ask_initial - P_median)，其中 ΔP_ask_treatment 为强制显示均价组卖家的平均挂价下调幅度，ΔP_ask_control 为对照组；基于某二手平台 2022 年 3 月的 A/B 测试数据，α_info 的 95% 置信区间为 [0.28, 0.42]，点估计值为 0.35。

## Corrected Claim

信息敏感度系数 α_info 的实证校准公式定义为：α_info = (ΔP_ask_treatment - ΔP_ask_control) / (P_ask_initial - P_median)。具体数值需依据特定实验数据确定，当前缺乏可靠来源支持其具体点估计值及置信区间。

## Evidence

[质询]该陈述包含具体的实证数据（2022年3月某二手平台A/B测试、具体的置信区间[0.28, 0.42]和点估计0.35），属于经验事实。在缺乏任何参考来源支持的情况下，无法验证这些具体数值的真实性，存在编造或幻觉风险。 | 经验事实，逻辑自洽但缺来源支持。公式定义在逻辑上合理（处理组与对照组之差除以基准价差），但具体数值（0.35, [0.28, 0.42]）及数据来源（2022年3月某平台）无任何检索结果佐证，无法确认为真实存在的实证结果。

## Search Query

A/B test forced display median price seller price adjustment alpha info coefficient 95% confidence interval
