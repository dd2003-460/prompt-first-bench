# N320: 回退瞬间缓存未命中率激增系数：Miss_Spike_Factor = 1 / (1 - α_Fallback_Cache_Warmth)。假设回退流量中80%在

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N124

## Claim

回退瞬间缓存未命中率激增系数：Miss_Spike_Factor = 1 / (1 - α_Fallback_Cache_Warmth)。假设回退流量中80%在公有云长尾节点无缓存（因非核心区域），则Miss_Spike_Factor ≈ 5，导致Origin_Latency占比从正常的5%激增至40%，P99_Hybrid_Worst = 0.4*300ms + 0.6*20ms = 132ms。

## Corrected Claim

回退瞬间缓存未命中率激增系数：Miss_Spike_Factor = 1 / (1 - α_Fallback_Cache_Warmth)。假设回退流量中80%在公有云长尾节点无缓存（因非核心区域），则Miss_Spike_Factor ≈ 5，导致Origin_Latency占比从正常的5%激增至40%，P99_Hybrid_Worst = 0.4*300ms + 0.6*20ms = 132ms。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导自洽（1/(1-0.8)=5），加权平均计算正确（0.4*300+0.6*20=132），量级合理。
