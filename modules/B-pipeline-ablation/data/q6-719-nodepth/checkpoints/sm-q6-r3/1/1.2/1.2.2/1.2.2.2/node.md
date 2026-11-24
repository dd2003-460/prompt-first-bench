# N157: Pareto 分布下 P99 延迟的长尾修正：若 RTT 服从 Pareto 分布（形状参数 α > 1），则 P99 = x_min / (0.01)^(1/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Pareto 分布下 P99 延迟的长尾修正：若 RTT 服从 Pareto 分布（形状参数 α > 1），则 P99 = x_min / (0.01)^(1/α)。对于网络延迟，α 通常在 1.5-2.5 之间，导致 P99 远大于均值，需通过尾部拟合确定 α。

## Corrected Claim

Pareto 分布下 P99 延迟的长尾修正：若 RTT 服从 Pareto 分布（形状参数 α > 1），则 P99 = x_min / (0.01)^(1/α)。对于网络延迟，α 通常在 1.5-2.5 之间，导致 P99 远大于均值，需通过尾部拟合确定 α。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的P99公式推导正确，α取值范围符合网络延迟长尾特征的经验规律

## Search Query

pareto distribution network latency tail shape parameter alpha
