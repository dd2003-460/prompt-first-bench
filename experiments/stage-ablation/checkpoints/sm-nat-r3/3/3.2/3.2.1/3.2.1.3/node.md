# N120: 边界条件：当 ρ → 0 时，E[S|Top10%] → E[S] = 11 KB；当 ρ → -1 时，E[S|Top10%] → x_min * 1.1，表

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N49

## Claim

边界条件：当 ρ → 0 时，E[S|Top10%] → E[S] = 11 KB；当 ρ → -1 时，E[S|Top10%] → x_min * 1.1，表明负相关越强，头部对象越小，缓存容量效率越高。

## Corrected Claim

边界条件：当 ρ → 0 时，E[S|Top10%] → E[S] = 11 KB；当 ρ → -1 时，E[S|Top10%] → x_min * 1.1，表明负相关越强，头部对象越小，缓存容量效率越高。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Effect of correlation strength on conditional size distribution
