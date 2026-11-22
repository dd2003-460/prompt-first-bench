# N138: 工作点 3 的 S_hot/S_total ≈ 0.8 是一个粗略估计。精确值需计算 Top-k_large 对象（即驻留在 128GB 缓存中的大对象）的字节

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

工作点 3 的 S_hot/S_total ≈ 0.8 是一个粗略估计。精确值需计算 Top-k_large 对象（即驻留在 128GB 缓存中的大对象）的字节流量占比。由于 α=1.1 接近 1，字节流量高度集中在头部。若缓存容纳了前 0.1% 的对象（N*0.001 = 100 个对象），其字节占比 B(100) 可通过 Pareto CDF 的字节加权形式计算：B(k) ≈ 1 - (k/N)^(1-α+1) 的近似变体，或更准确地通过 ∫_{s_min}^{s_k} s * f_S(s) ds / ∫_{s_min}^{∞} s * f_S(s) ds 数值积分得出。该值直接线性影响 ΔH 的最终结果。

## Corrected Claim

工作点 3 的 S_hot/S_total ≈ 0.8 是一个粗略估计。精确值需计算 Top-k_large 对象（即驻留在 128GB 缓存中的大对象）的字节流量占比。由于 α=1.1 接近 1，字节流量高度集中在头部。若缓存容纳了前 0.1% 的对象（N*0.001 = 100 个对象），其字节占比 B(100) 可通过 Pareto CDF 的字节加权形式计算：B(k) ≈ 1 - (k/N)^(1-α+1) 的近似变体，或更准确地通过 ∫_{s_min}^{s_k} s * f_S(s) ds / ∫_{s_min}^{∞} s * f_S(s) ds 数值积分得出。该值直接线性影响 ΔH 的最终结果。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Pareto distribution byte fraction top k objects alpha 1.1
