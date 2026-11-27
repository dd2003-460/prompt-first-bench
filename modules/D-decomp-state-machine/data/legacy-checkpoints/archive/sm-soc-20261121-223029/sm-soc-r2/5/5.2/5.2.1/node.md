# N100: 成交均价与成交周期的相关性系数 r = corr(P_deal, T_cycle)，在 δ ∈ [0.15, 0.25] 样本区间内需计算具体数值；若 r < 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

成交均价与成交周期的相关性系数 r = corr(P_deal, T_cycle)，在 δ ∈ [0.15, 0.25] 样本区间内需计算具体数值；若 r < 0.3 则判定随机偏好噪声导致周期缩短的假设置信度 < 0.5。

## Corrected Claim

成交均价与成交周期的相关性系数 r = corr(P_deal, T_cycle) 需在 δ ∈ [0.15, 0.25] 样本区间内计算具体数值；若 r < 0.3，通常提示随机偏好噪声导致周期缩短的假设支持度较弱（具体置信度需结合样本量及统计检验结果确定）。

## Evidence

[质询]该陈述包含具体的经验性阈值（r < 0.3 对应置信度 < 0.5），这属于统计推断中的经验规则或特定模型假设，无法从第一性原理或数学公理中严格推导出来，且缺乏具体的统计检验方法（如t检验、p值计算）支持该特定映射关系。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该阈值映射非数学恒等式，属经验性统计判断）

## Search Query

used goods platform correlation between transaction price and cycle time high premium items
