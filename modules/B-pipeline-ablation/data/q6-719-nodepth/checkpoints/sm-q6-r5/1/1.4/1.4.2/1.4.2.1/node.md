# N150: 缓存预热状态对 A_p99 的量化影响：设预热完成度 W_cache ∈ [0,1]。未预热时（W_cache=0），回源率 R_back=100%，L_p99

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

缓存预热状态对 A_p99 的量化影响：设预热完成度 W_cache ∈ [0,1]。未预热时（W_cache=0），回源率 R_back=100%，L_p99_peak ≈ L_backhaul + L_edge ≈ 150ms，L_p99_avg ≈ 50ms，A_p99 = (150-50)/50 = 2.0。完全预热时（W_cache=1），回源率 R_back=10%，L_p99_peak ≈ 50ms，L_p99_avg ≈ 50ms，A_p99 ≈ 0.0。线性插值模型：A_p99(W_cache) = 2.0 * (1 - W_cache)^1.5，其中指数 1.5 反映长尾对象预热滞后效应。

## Corrected Claim

缓存预热状态对 A_p99 的量化影响：设预热完成度 W_cache ∈ [0,1]。未预热时（W_cache=0），回源率 R_back=100%，L_p99_peak ≈ L_backhaul + L_edge ≈ 150ms，L_p99_avg ≈ 50ms，A_p99 = (150-50)/50 = 2.0。完全预热时（W_cache=1），回源率 R_back=10%，L_p99_peak ≈ 50ms，L_p99_avg ≈ 50ms，A_p99 ≈ 0.0。线性插值模型：A_p99(W_cache) = 2.0 * (1 - W_cache)^1.5，其中指数 1.5 反映长尾对象预热滞后效应。

## Evidence

先验知识/题面给定，逻辑校验通过
