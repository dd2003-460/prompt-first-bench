# N64: 平台驱动性的量化边界：平台对均衡的驱动强度定义为 ∂(Equilibrium_Stability)/∂w_signal。若该偏导数在 w_signal ∈ [0

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N13

## Claim

平台驱动性的量化边界：平台对均衡的驱动强度定义为 ∂(Equilibrium_Stability)/∂w_signal。若该偏导数在 w_signal ∈ [0.2, 0.5] 区间内显著为正（p<0.01），则平台是均衡形成的关键驱动者；若接近 0，则平台仅为被动中介。

## Corrected Claim

平台驱动性的量化边界：平台对均衡的驱动强度定义为 ∂(Equilibrium_Stability)/∂w_signal。若该偏导数在 w_signal ∈ [0.2, 0.5] 区间内显著为正（p<0.01），则平台是均衡形成的关键驱动者；若接近 0，则平台仅为被动中介。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上覆盖了输入估计（N1）、核心推导（N2）和统计检验（N3），三者正交且无冗余。但存在关键遗漏：父节点定义中明确限定了 w_signal 的区间为 [0.2, 0.5]，并强调“在该区间内显著为正”。然而，三个子节点均未涉及“区间边界条件”或“区间内单调性/稳定性”的量化分解。例如，N2 仅给出解析表达式，未说明如何验证其在 [0.2, 0.5] 内的行为；N3 的 t_stat 是点估计检验，未覆盖区间内整体显著性（如置信区间是否完全位于正域）。因此，完备性不足。）
