# N260: 计算字节命中率分子 Σ_{i=1}^{K_eff} p_i * s_i：利用 Zipf 分布 p_i = i^{-0.9}/H(N, 0.9) 和 Pareto

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97, N98

## Claim

计算字节命中率分子 Σ_{i=1}^{K_eff} p_i * s_i：利用 Zipf 分布 p_i = i^{-0.9}/H(N, 0.9) 和 Pareto 大小分布 s_i（受 ρ=-0.3 修正），计算前 K_eff 个对象贡献的加权字节数，该值直接决定命中率上限。

## Corrected Claim

计算字节命中率分子 Σ_{i=1}^{K_eff} p_i * s_i：利用 Zipf 分布 p_i = i^{-0.9}/H(N, 0.9) 和 Pareto 大小分布 s_i（受 ρ=-0.3 修正），计算前 K_eff 个对象贡献的加权字节数，该值直接决定命中率上限。

## Evidence

先验知识/题面给定，逻辑校验通过：字节命中率分子定义为命中对象的加权字节数之和，公式 Σ p_i * s_i 符合定义，Zipf 和 Pareto 分布参数在缓存模型中量级合理。
