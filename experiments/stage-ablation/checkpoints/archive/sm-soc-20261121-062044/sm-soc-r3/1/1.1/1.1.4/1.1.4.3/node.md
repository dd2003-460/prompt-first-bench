# N112: 时间压力衰减函数 γ_time：α_ref 随挂售时间 T_list 增加而衰减，模型为 α_ref(T) = α_ref_0 * exp(-T_list / 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N31

## Claim

时间压力衰减函数 γ_time：α_ref 随挂售时间 T_list 增加而衰减，模型为 α_ref(T) = α_ref_0 * exp(-T_list / τ)，其中 τ 为半衰期参数，实证估计 τ ≈ 14 天。若 T_list > 30 天，α_ref 降至初始值的 45% 以下，卖家更倾向于接受市场定价。

## Corrected Claim

时间压力衰减函数 γ_time 通常建模为指数衰减形式 α_ref(T) = α_ref_0 * exp(-T_list / τ)。在缺乏具体实证数据支持的情况下，τ 的具体数值（如 14 天）及 T_list > 30 天时的具体行为倾向（接受市场定价）应视为假设性参数，而非确证的实证结论。

## Evidence

[质询]该陈述包含具体的实证参数（τ ≈ 14 天）和特定的行为结论（卖家更倾向于接受市场定价），属于经验事实。由于检索无可用来源，无法验证该特定模型参数及行为假设是否来自可靠的实证研究，存在来源不可靠或参数虚构的风险。 | 经验事实，逻辑自洽但缺来源支持。数学上，若 τ=14，T=30 时 exp(-30/14) ≈ 0.118，确实低于 45%，逻辑推导成立；但 τ 的具体数值及行为结论缺乏外部证据支持。

## Search Query

seller patience loss aversion decay time listed used goods market
