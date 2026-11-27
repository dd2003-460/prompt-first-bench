# N228: 参数 k_sens（卖家敏感度）的回归估计方法：通过面板数据模型 ΔP_ask_it = k_sens * (P_ask_it - P_median_t) * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

参数 k_sens（卖家敏感度）的回归估计方法：通过面板数据模型 ΔP_ask_it = k_sens * (P_ask_it - P_median_t) * P(ReadLabel_it) + ε_it 进行 OLS 回归，k_sens 的标准误需通过 Newey-West 校正以处理序列相关；若 k_sens 的 95% 置信区间包含 0，则拒绝干预有效假设。

## Corrected Claim

参数 k_sens（卖家敏感度）的回归估计方法：通过面板数据模型 ΔP_ask_it = k_sens * (P_ask_it - P_median_t) * P(ReadLabel_it) + ε_it 进行 OLS 回归，k_sens 的标准误需通过 Newey-West 校正以处理序列相关；若 k_sens 的 95% 置信区间包含 0，则拒绝干预有效假设。

## Evidence

先验知识/题面给定，逻辑校验通过：面板数据回归中处理序列相关使用Newey-West校正是标准计量经济学做法，且置信区间包含0即无法拒绝原假设（此处原假设为无效/零效应）符合统计推断逻辑。

## Search Query

seller price sensitivity regression panel data Newey-West correction
