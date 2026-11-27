# N113: 基于修正后的 T_res（由 N61 计算得出），失效概率 P_invalid 的重新计算值：P_invalid = 1 - exp(-0.01 * T_res

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

基于修正后的 T_res（由 N61 计算得出），失效概率 P_invalid 的重新计算值：P_invalid = 1 - exp(-0.01 * T_res_corrected)；若 T_res_corrected ≈ 2 days，则 P_invalid ≈ 1.98%，显著低于 N39 原估算的 9.516%，这直接决定了 (c) 问中 LRU 命中率打折幅度的准确下限。

## Corrected Claim

基于修正后的 T_res（由 N61 计算得出），失效概率 P_invalid 的重新计算值：P_invalid = 1 - exp(-0.01 * T_res_corrected)；若 T_res_corrected ≈ 2 days，则 P_invalid ≈ 1.98%，显著低于 N39 原估算的 9.516%，这直接决定了 (c) 问中 LRU 命中率打折幅度的准确下限。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - exp(-0.01 * 2) ≈ 0.0198 (1.98%) 正确，且与 9.516% 的对比符合逻辑。
