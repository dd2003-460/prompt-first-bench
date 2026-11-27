# N71: k_eff 对象的总字节量 S_eff = ∫_{top k_eff} S_i di；由于 ρ=-0.3（热度与大小负相关），这 6700 个热门对象的平均大小

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

k_eff 对象的总字节量 S_eff = ∫_{top k_eff} S_i di；由于 ρ=-0.3（热度与大小负相关），这 6700 个热门对象的平均大小 E[S|Top_k_eff] 小于全局平均 E[S]≈11KB；估算 E[S|Top_k_eff] ≈ E[S] * (1 + ρ * σ_logS * σ_logH) ≈ 11KB * (1 - 0.3*1.5*1.5) ≈ 5KB；因此 S_eff ≈ 6700 * 5KB ≈ 33.5 MB，远小于 128GB 缓存容量，证实缓存容量完全由‘热度’而非‘大小’瓶颈限制。

## Corrected Claim

k_eff 对象的总字节量 S_eff = ∫_{top k_eff} S_i di；由于 ρ=-0.3（热度与大小负相关），这 6700 个热门对象的平均大小 E[S|Top_k_eff] 小于全局平均 E[S]≈11KB；估算 E[S|Top_k_eff] ≈ E[S] * (1 + ρ * σ_logS * σ_logH) ≈ 11KB * (1 - 0.3*1.5*1.5) ≈ 5KB；因此 S_eff ≈ 6700 * 5KB ≈ 33.5 MB，远小于 128GB 缓存容量，证实缓存容量完全由‘热度’而非‘大小’瓶颈限制。

## Evidence

父节点级核验未通过：有冗余（子节点本质上是同一公式在不同参数取值下的计算结果（敏感性分析/场景分析），而非逻辑上独立的关键方面。虽然它们在参数空间上不重叠（正交），但结构上高度冗余，因为它们共享完全相同的推导逻辑和公式，仅输入变量不同。完备性方面，覆盖了保守、标准和悲观三种情况，逻辑上完整。）
