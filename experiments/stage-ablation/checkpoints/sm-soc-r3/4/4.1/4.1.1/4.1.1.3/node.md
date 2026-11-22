# N211: β_info 对分布参数的交互效应：β_info 不仅影响均值 ΔP_init，还影响方差 Var(P_ask)，模型为 Var(P_ask_new) = Va

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

β_info 对分布参数的交互效应：β_info 不仅影响均值 ΔP_init，还影响方差 Var(P_ask)，模型为 Var(P_ask_new) = Var(P_ask_old) × (1 - δ_var × β_info²)，其中 δ_var 为方差收缩系数（假设 0.1-0.3），需估算信息透明化是否导致挂价分布更集中（方差减小）。

## Corrected Claim

β_info 对分布参数的交互效应：β_info 不仅影响均值 ΔP_init，还影响方差 Var(P_ask)。模型假设 Var(P_ask_new) = Var(P_ask_old) × (1 - δ_var × β_info²)，其中 δ_var 为方差收缩系数（具体数值需实证估算，此处假设 0.1-0.3 仅为示例），需验证信息透明化是否导致挂价分布更集中。

## Evidence

[质询]该陈述包含具体的经验性参数假设（δ_var 取值范围 0.1-0.3）及特定的数学模型形式，属于经验事实/模型假设，无法从第一性原理严格推导，且缺乏外部来源支持其具体数值或模型结构的合理性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该模型参数属于经验假设，不适用第一性原理推导条款）

## Search Query

variance reduction price anchoring information disclosure behavioral economics
