# N151: 回源带宽余量对 A_p99 的约束边界：设回源链路利用率 U_backhaul = T_backhaul / B_backhaul_capacity。当 U_b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

回源带宽余量对 A_p99 的约束边界：设回源链路利用率 U_backhaul = T_backhaul / B_backhaul_capacity。当 U_backhaul < 0.6 时，队列延迟可忽略，A_p99 主要由传播延迟决定，稳定在 0.5 左右；当 U_backhaul > 0.8 时，排队延迟呈指数增长（M/M/1 模型），A_p99 急剧上升至 1.5-3.0。临界点 U_crit ≈ 0.75，此时需增加回源带宽 B_redundant = B_base * (1/U_target - 1)，其中 U_target=0.6 为安全阈值。

## Corrected Claim

回源带宽余量对 A_p99 的约束边界：设回源链路利用率 U_backhaul = T_backhaul / B_backhaul_capacity。当 U_backhaul < 0.6 时，队列延迟可忽略，A_p99 主要由传播延迟决定，稳定在 0.5 左右；当 U_backhaul > 0.8 时，排队延迟呈指数增长（M/M/1 模型），A_p99 急剧上升至 1.5-3.0。临界点 U_crit ≈ 0.75，此时需增加回源带宽 B_redundant = B_base * (1/U_target - 1)，其中 U_target=0.6 为安全阈值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应排队论模型（机制）、带宽计算公式（工程实现）和稳定性边界/成本权衡（决策依据），三者逻辑维度不同，互不重叠且无矛盾。虽然都涉及 U_backhaul 和 A_p99，但侧重点分别为微观延迟计算、宏观资源配比和宏观性能阈值，覆盖了父节点关于约束边界、临界点和冗余配置的所有关键方面。）
