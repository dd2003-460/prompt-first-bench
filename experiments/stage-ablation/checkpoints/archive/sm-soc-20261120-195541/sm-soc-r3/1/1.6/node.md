# N10: 利益相关方驱动判定指标：定义驱动者强度 D_i = ∂(Equilibrium Stability)/∂(Strategy_i)，其中 i ∈ {B, S, P

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

利益相关方驱动判定指标：定义驱动者强度 D_i = ∂(Equilibrium Stability)/∂(Strategy_i)，其中 i ∈ {B, S, P}，若 D_S > D_B 且 D_S > D_P，则卖家为主要驱动者；依据是卖家挂价策略对均衡稳定性的偏导数最大，因为卖家通过高挂价+短周期获得更高的期望收益，而买家和平台的策略调整对均衡影响较小。

## Corrected Claim

利益相关方驱动判定指标：定义驱动者强度 D_i = ∂(Equilibrium Stability)/∂(Strategy_i)，其中 i ∈ {B, S, P}，若 D_S > D_B 且 D_S > D_P，则卖家为主要驱动者；依据是卖家挂价策略对均衡稳定性的偏导数最大，因为卖家通过高挂价+短周期获得更高的期望收益，而买家和平台的策略调整对均衡影响较小。

## Evidence

父节点级核验未通过：不完备（子节点覆盖了均衡稳定性定义、卖家驱动强度计算和平台驱动强度计算，三者之间无重复或矛盾（正交性合格）。然而，父节点明确定义 i ∈ {B, S, P}（买家、卖家、平台），且判定条件涉及 D_S > D_B 和 D_S > D_P，但子节点中缺失了买家驱动强度 D_B 的计算公式或定义，导致无法完整执行父节点所述的‘主要驱动者’判定逻辑，因此完备性不足。）

## Search Query

equilibrium stability derivative stakeholder strategy marketplace
