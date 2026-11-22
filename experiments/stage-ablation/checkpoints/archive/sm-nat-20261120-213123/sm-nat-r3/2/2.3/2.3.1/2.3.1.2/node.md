# N98: 修正 N39 的计算错误：σ_logS = √(Var[log S]) = 1/α = 1/1.1 ≈ 0.9091。父节点中使用的 π/α ≈ 2.856 是

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

修正 N39 的计算错误：σ_logS = √(Var[log S]) = 1/α = 1/1.1 ≈ 0.9091。父节点中使用的 π/α ≈ 2.856 是 Zeta 分布或特定离散模型的特征，不适用于连续 Pareto 的对数方差计算。

## Corrected Claim

修正 N39 的计算错误：σ_logS = √(Var[log S]) = 1/α = 1/1.1 ≈ 0.9091。父节点中使用的 π/α ≈ 2.856 是 Zeta 分布或特定离散模型的特征，不适用于连续 Pareto 的对数方差计算。

## Evidence

先验知识/题面给定，逻辑校验通过：连续Pareto分布（形状参数α）的对数方差确实为1/α²，标准差为1/α，与陈述一致。
