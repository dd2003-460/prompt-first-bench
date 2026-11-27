# N140: 短窗口高污染工作点（Short-T/High-Pollution）：当时间窗口 T 远小于 LRU 驱逐周期（T << T_evict）时，被驱逐对象立即被再次

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

短窗口高污染工作点（Short-T/High-Pollution）：当时间窗口 T 远小于 LRU 驱逐周期（T << T_evict）时，被驱逐对象立即被再次访问，P_pollution ≈ P_miss_LRU ≈ 0.88，此时 LFU 若能保留这些高频对象，其理论增益 ΔH ≈ P_pollution * (1 - P_invalid) ≈ 0.88，代表污染损失的最大潜在价值。

## Corrected Claim

短窗口高污染工作点（Short-T/High-Pollution）：当时间窗口 T 远小于 LRU 驱逐周期（T << T_evict）时，被驱逐对象立即被再次访问，P_pollution ≈ P_miss_LRU ≈ 0.88，此时 LFU 若能保留这些高频对象，其理论增益 ΔH ≈ P_pollution * (1 - P_invalid) ≈ 0.88，代表污染损失的最大潜在价值。

## Evidence

先验知识/题面给定，逻辑校验通过
