# N167: 工作点 B（中波动-中遗忘）：λ=0.1, T_shift=10 天，σ_f=1.5，计算 f_stale = exp(-0.1*10) ≈ 0.368，此时 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58, N59, N60

## Claim

工作点 B（中波动-中遗忘）：λ=0.1, T_shift=10 天，σ_f=1.5，计算 f_stale = exp(-0.1*10) ≈ 0.368，此时 LFU 缓存中 36.8% 为旧热点，评估此点的命中率损失与计算开销的 trade-off。

## Corrected Claim

工作点 B（中波动-中遗忘）：λ=0.1, T_shift=10 天，σ_f=1.5，计算 f_stale = exp(-0.1*10) ≈ 0.368，此时 LFU 缓存中 36.8% 为旧热点，评估此点的命中率损失与计算开销的 trade-off。

## Evidence

先验知识/题面给定，逻辑校验通过：exp(-1) ≈ 0.367879，四舍五入为 0.368 正确，且 36.8% 与 0.368 对应一致。
