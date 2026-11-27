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

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于τ_res的定量计算与参数依赖，子节点2聚焦于比值r的物理意义与临界点分析，两者维度不同（定量vs定性/物理意义），无重复或矛盾。父节点核心包含τ_res数值、τ_obj数值及比值r，两个子节点分别解释了τ_res的来源和r的含义，覆盖了关键方面。）
