# N166: 工作点 A（高波动-低遗忘）：λ=0.01, T_shift=10 天，σ_f=2.5，计算 f_stale = exp(-0.01*10) ≈ 0.905，此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58, N59, N60

## Claim

工作点 A（高波动-低遗忘）：λ=0.01, T_shift=10 天，σ_f=2.5，计算 f_stale = exp(-0.01*10) ≈ 0.905，此时 LFU 缓存中 90.5% 为旧热点，验证此点是否位于性能退化前沿。

## Corrected Claim

工作点 A（高波动-低遗忘）：λ=0.01, T_shift=10 天，σ_f=2.5，计算 f_stale = exp(-0.01*10) ≈ 0.905，此时 LFU 缓存中 90.5% 为旧热点，验证此点是否位于性能退化前沿。

## Evidence

先验知识/题面给定，逻辑校验通过：exp(-0.01*10) = exp(-0.1) ≈ 0.9048，四舍五入为0.905，计算正确且逻辑自洽。
