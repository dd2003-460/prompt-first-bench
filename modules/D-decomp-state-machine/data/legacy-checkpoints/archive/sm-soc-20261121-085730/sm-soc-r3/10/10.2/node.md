# N145: 挂价上限提升幅度 ΔP_anchor 的动态演化公式：ΔP_anchor(t+1) = ρ * ΔP_anchor(t) + σ_noise * ξ(t)，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

挂价上限提升幅度 ΔP_anchor 的动态演化公式：ΔP_anchor(t+1) = ρ * ΔP_anchor(t) + σ_noise * ξ(t)，其中 ρ 为从众惯性系数（0<ρ<1），σ_noise 为随机偏好噪声标准差，ξ(t) 为标准正态随机变量，用于模拟价格泡沫的自我强化过程。

## Corrected Claim

挂价上限提升幅度 ΔP_anchor 的动态演化公式：ΔP_anchor(t+1) = ρ * ΔP_anchor(t) + σ_noise * ξ(t)，其中 ρ 为从众惯性系数（0<ρ<1），σ_noise 为随机偏好噪声标准差，ξ(t) 为标准正态随机变量，用于模拟价格泡沫的自我强化过程。

## Evidence

父节点级核验通过：正交+完备+无冗余（父节点公式包含两个核心参数：从众惯性系数 ρ 和随机噪声标准差 σ_noise。两个子节点分别针对这两个参数提供了独立的估计/计算方法，彼此之间没有重叠（正交），且共同覆盖了父节点公式中所有需要动态演化的关键参数（完备）。两者分别处理确定性趋势（惯性）和随机性（噪声），不存在冗余。）

## Search Query

price bubble dynamics herding behavior stochastic process
