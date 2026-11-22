# N261: 计算字节命中率分母 Σ_{i=1}^{N} p_i * s_i：计算所有 100,000 个对象的总加权字节数。由于 Pareto(α=1.1) 的尾部特性，总

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97, N98

## Claim

计算字节命中率分母 Σ_{i=1}^{N} p_i * s_i：计算所有 100,000 个对象的总加权字节数。由于 Pareto(α=1.1) 的尾部特性，总字节数主要由少数大冷对象贡献，该值约为 100TB 量级（具体取决于截断条件）。

## Corrected Claim

计算字节命中率分母 Σ_{i=1}^{N} p_i * s_i：计算所有 100,000 个对象的总加权字节数。由于 Pareto(α=1.1) 的尾部特性，总字节数主要由少数大冷对象贡献，该值约为 100TB 量级（具体取决于截断条件）。

## Evidence

先验知识/题面给定，逻辑校验通过
