# N18: 缓存中对象平均驻留时间 τ_res ≈ 100 天（假设 LRU 淘汰主导），与对象平均失效时间 τ_obj = 100 天 的比值 r = τ_res / τ

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

缓存中对象平均驻留时间 τ_res ≈ 100 天（假设 LRU 淘汰主导），与对象平均失效时间 τ_obj = 100 天 的比值 r = τ_res / τ_obj = 1.0。

## Corrected Claim

缓存中对象平均驻留时间 τ_res ≈ 100 天（假设 LRU 淘汰主导），与对象平均失效时间 τ_obj = 100 天 的比值 r = τ_res / τ_obj = 1.0。

## Evidence

先验知识/题面给定，逻辑校验通过：比值计算 100/100=1.0 正确，且符合 LRU 缓存中对象驻留时间与失效时间量级相当的工程直觉。
