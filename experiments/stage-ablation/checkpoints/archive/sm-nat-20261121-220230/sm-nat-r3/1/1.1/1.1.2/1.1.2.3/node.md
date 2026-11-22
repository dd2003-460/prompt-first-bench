# N109: Pareto 分布尾部截断对 E[s] 的修正因子：F_tail = E[s]_truncated / E[s]_infinite，其中 E[s]_infini

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Pareto 分布尾部截断对 E[s] 的修正因子：F_tail = E[s]_truncated / E[s]_infinite，其中 E[s]_infinite 在 α≤1 时发散，该因子量化了 s_max=100MB 假设对分母有限性的贡献。

## Corrected Claim

Pareto 分布尾部截断对 E[s] 的修正因子：F_tail = E[s]_truncated / E[s]_infinite，其中 E[s]_infinite 在 α≤1 时发散，该因子量化了 s_max=100MB 假设对分母有限性的贡献。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布尾部截断确实通过限制积分上限使期望收敛，该因子定义符合概率论中截断分布期望与原始分布期望（若收敛）或发散性的对比逻辑。
