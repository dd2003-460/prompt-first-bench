# N141: 并行化加速比公式的适用边界条件：公式 Speedup = min(N_seq, 1/(1+T_comm/T_compute)) 仅在T_compute远大于T_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

并行化加速比公式的适用边界条件：公式 Speedup = min(N_seq, 1/(1+T_comm/T_compute)) 仅在T_compute远大于T_comm且无显存竞争时成立；当8序列并发导致KV Cache显存占用超过单卡可用上限（10.5GB）时，需启用Swap或Preemption，此时有效加速比将低于理论值，需引入显存压力系数η。

## Corrected Claim

并行化加速比公式的适用边界条件：公式 Speedup = min(N_seq, 1/(1+T_comm/T_compute)) 仅在T_compute远大于T_comm且无显存竞争时成立；当8序列并发导致KV Cache显存占用超过单卡可用上限（10.5GB）时，需启用Swap或Preemption，此时有效加速比将低于理论值，需引入显存压力系数η。

## Evidence

先验知识/题面给定，逻辑校验通过
