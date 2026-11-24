# N75: 公有云 CDN 缓存命中率 CHR_pub 对 B_served 的影响：B_served = B_total × (1 - CHR_pub)。公有云 CDN 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

公有云 CDN 缓存命中率 CHR_pub 对 B_served 的影响：B_served = B_total × (1 - CHR_pub)。公有云 CDN 因全球节点共享，CHR_pub 通常为 85-90%。需量化 CHR_pub 从 80% 增至 90% 时，B_served 降低 11.1%，对应带宽成本降低 11.1%。

## Corrected Claim

公有云 CDN 缓存命中率 CHR_pub 对 B_served 的影响：B_served = B_total × (1 - CHR_pub)。公有云 CDN 因全球节点共享，CHR_pub 通常为 85-90%。需量化 CHR_pub 从 80% 增至 90% 时，B_served 降低 50%，对应带宽成本降低 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导 (1-0.9)/(1-0.8) = 0.1/0.2 = 0.5，即降低50%？不对，重新计算：B_served_old = B_total * (1-0.8) = 0.2 * B_total; B_served_new = B_total * (1-0.9) = 0.1 * B_total. 降低比例 = (0.2 - 0.1) / 0.2 = 50%。等等，题目说降低11.1%。让我们再仔细看一遍题目陈述：“需量化 CHR_pub 从 80% 增至 90% 时，B_served 降低 11.1%”。

计算：
初始 B_served = B_total * (1 - 0.80) = 0.20 * B_total
最终 B_served = B_total * (1 - 0.90) = 0.10 * B_total
变化量 = 0.10 - 0.20 = -0.10 * B_total
降低百分比 = (0.10 / 0.20) * 100% = 50%。

题目中声称降低 11.1% 是错误的。11.1% 通常是 1/9 的近似值，或者可能是混淆了其他计算（例如从 90% 到 80% 的相对变化？或者误用了公式？）。如果 CHR 从 80% 增加到 90%，未命中流量从 20% 降到 10%，确实是减半，即降低 50%。

因此，该陈述存在硬逻辑/数学错误。
