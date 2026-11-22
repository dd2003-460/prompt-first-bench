# N28: 共享随机源：活跃挂牌数量 N_active_listings 的动态变化率 ΔN/Δt 受卖家退出率 μ_exit 和进入率 μ_entry 影响，其中 μ_e

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

共享随机源：活跃挂牌数量 N_active_listings 的动态变化率 ΔN/Δt 受卖家退出率 μ_exit 和进入率 μ_entry 影响，其中 μ_exit = f(T_deal, P_ask)，具体为 μ_exit = k_exit * (T_deal/T_max)^γ，k_exit 为退出敏感度，γ 为时间弹性（通常 γ > 1），该动态过程决定了 N_active_listings 的稳态值。

## Corrected Claim

共享随机源：活跃挂牌数量 N_active_listings 的动态变化率 ΔN/Δt 受卖家退出率 μ_exit 和进入率 μ_entry 影响，其中 μ_exit = f(T_deal, P_ask)，具体为 μ_exit = k_exit * (T_deal/T_max)^γ，k_exit 为退出敏感度，γ 为时间弹性（通常 γ > 1），该动态过程决定了 N_active_listings 的稳态值。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了一个标准的动态平衡模型（进入率与退出率决定稳态），其中退出率随挂牌时间增加而加速（γ>1符合直觉，即挂得越久越容易因过时或失去耐心而退出），量纲和逻辑自洽，无内部矛盾。

## Search Query

dynamic listing inventory exit rate marketplace
