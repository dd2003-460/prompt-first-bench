# N234: E[S|Cold] 在 ρ=-0.3 下的计算：Cold 指未被缓存对象（若 k<1），其平均大小 E[S|Cold] = E[S] / (1 - (1-k)^

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N85

## Claim

E[S|Cold] 在 ρ=-0.3 下的计算：Cold 指未被缓存对象（若 k<1），其平均大小 E[S|Cold] = E[S] / (1 - (1-k)^{1-α_eff})，由于 α=1.1 接近 1，尾部贡献大，若 k=0.1，E[S|Cold] ≈ 0.9 * E[S]，导致 H_LRU_lb 显著低于请求命中率。

## Corrected Claim

E[S|Cold] 在 ρ=-0.3 下的计算：Cold 指未被缓存对象（若 k<1），其平均大小 E[S|Cold] = E[S] / (1 - (1-k)^{1-α_eff})。由于 α=1.1 接近 1，尾部贡献大，若 k=0.1，E[S|Cold] ≈ 95 * E[S]（具体数值取决于 α_eff 的精确值），导致 H_LRU_lb 显著低于请求命中率。

## Evidence

[质询]公式推导与数值结论存在逻辑矛盾：若 α=1.1 且 k=0.1，根据给定的公式 E[S|Cold] = E[S] / (1 - (1-k)^{1-α_eff})，分母约为 1 - 0.9^{0.1} ≈ 0.0105，导致 E[S|Cold] ≈ 95 * E[S]，而非陈述中声称的 0.9 * E[S]。陈述中的数值结论与公式及参数严重不符。 | 先验知识/题面给定，逻辑校验发现公式计算结果与陈述数值结论矛盾（95倍 vs 0.9倍），且无外部来源支持该特定数值结论。
