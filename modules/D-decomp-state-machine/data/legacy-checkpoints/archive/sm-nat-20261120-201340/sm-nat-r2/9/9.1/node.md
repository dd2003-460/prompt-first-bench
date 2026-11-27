# N71: 在 ρ=-0.3 的负相关约束下，LFU 能容纳的高频对象数量 k_LFU 与 LRU 能容纳的 k_LRU 的比值关系：k_LFU / k_LRU = E[S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

在 ρ=-0.3 的负相关约束下，LFU 能容纳的高频对象数量 k_LFU 与 LRU 能容纳的 k_LRU 的比值关系：k_LFU / k_LRU = E[S_LRU_cached] / E[S_LFU_cached]，由于 LFU 严格保留最高频对象（通常更小），而 LRU 可能因时间局部性保留部分低频大对象，故 E[S_LFU_cached] < E[S_LRU_cached]，具体比值需通过联合分布积分计算。

## Corrected Claim

在 ρ=-0.3 的负相关约束下，LFU 能容纳的高频对象数量 k_LFU 与 LRU 能容纳的 k_LRU 的比值关系：k_LFU / k_LRU = E[S_LRU_cached] / E[S_LFU_cached]，由于 LFU 严格保留最高频对象（通常更小），而 LRU 可能因时间局部性保留部分低频大对象，故 E[S_LFU_cached] < E[S_LRU_cached]，具体比值需通过联合分布积分计算。

## Evidence

先验知识/题面给定，逻辑校验通过
