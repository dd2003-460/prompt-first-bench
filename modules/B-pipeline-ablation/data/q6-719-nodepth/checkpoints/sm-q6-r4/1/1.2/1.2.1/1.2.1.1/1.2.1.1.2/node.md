# N626: 基于修正后的公式 RTT_ms ≈ 0.05*d + 7.5，当 d_p99 = 300km 时，P99(RTT_user_edge) ≈ 0.05*300 +

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N205

## Claim

基于修正后的公式 RTT_ms ≈ 0.05*d + 7.5，当 d_p99 = 300km 时，P99(RTT_user_edge) ≈ 0.05*300 + 7.5 = 22.5ms，而非原估的 20ms，这 2.5ms 的差异在 T=100ms 约束下可能影响回源预算分配。

## Corrected Claim

基于修正后的公式 RTT_ms ≈ 0.05*d + 7.5，当 d_p99 = 300km 时，P99(RTT_user_edge) ≈ 0.05*300 + 7.5 = 22.5ms，而非原估的 20ms，这 2.5ms 的差异在 T=100ms 约束下可能影响回源预算分配。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.05*300 + 7.5 = 22.5 正确，且 22.5ms 与 20ms 的差异为 2.5ms，符合物理直觉与数学推导。
