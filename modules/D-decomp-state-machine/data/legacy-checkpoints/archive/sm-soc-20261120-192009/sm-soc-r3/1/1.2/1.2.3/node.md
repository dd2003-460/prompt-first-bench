# N40: 理性策略的临界条件：卖家选择高挂价 p_high > μ 的演化最优条件是 ∂U_seller/∂p > 0，即 E[ΔRevenue] > r * E[Δt_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

理性策略的临界条件：卖家选择高挂价 p_high > μ 的演化最优条件是 ∂U_seller/∂p > 0，即 E[ΔRevenue] > r * E[Δt_wait]，该不等式定义了高挂价策略的可行域。

## Corrected Claim

理性策略的临界条件：卖家选择高挂价 p_high > μ 的演化最优条件是 ∂U_seller/∂p > 0，即 E[ΔRevenue] > r * E[Δt_wait]，该不等式定义了高挂价策略的可行域。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于临界成本率r*的解析推导与阈值判断，子节点2聚焦于期望等待时间E[Δt_wait]的微观机制与信息不对称影响。两者分别处理不等式右侧的两个独立变量（r和E[Δt_wait]），逻辑正交且共同构成了父节点中不等式 E[ΔRevenue] > r * E[Δt_wait] 的完整解释框架。数值示例用于辅助理解，不构成冗余。）
