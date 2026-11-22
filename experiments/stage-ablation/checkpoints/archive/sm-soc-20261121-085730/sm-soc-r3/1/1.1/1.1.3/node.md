# N46: 高挂价规避损失的量化收益：ΔU_loss_aversion = λ * (P - C_ref) * Q(P)，其中Q(P)为成交概率，当P > C_ref时，该

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

高挂价规避损失的量化收益：ΔU_loss_aversion = λ * (P - C_ref) * Q(P)，其中Q(P)为成交概率，当P > C_ref时，该效用项为正，抵消降价带来的心理痛苦。

## Corrected Claim

高挂价规避损失的量化收益：ΔU_loss_aversion = λ * (P - C_ref) * Q(P)，其中Q(P)为成交概率，当P > C_ref时，该效用项为正，抵消降价带来的心理痛苦。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点2和3本质上是同一公式在不同参数下的数值实例，存在显著冗余；此外，父节点中定义的参数λ（损失厌恶系数）和C_ref（参考成本）在子节点中缺乏独立解释或定义节点，导致对父节点关键组成部分的覆盖不完备。）

## Search Query

loss aversion pricing strategy seller utility function transaction probability
