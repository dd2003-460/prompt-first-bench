# N174: P(rank_i ≤ K_max) 的量化计算：由于 K_max ≈ 98,500 且总对象数 N=100,000，该概率为 98.5%。但在 ρ=-0.3 的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

P(rank_i ≤ K_max) 的量化计算：由于 K_max ≈ 98,500 且总对象数 N=100,000，该概率为 98.5%。但在 ρ=-0.3 的负相关下，被更新的对象若为高频小对象，其 rank_i 更可能小于 K_max，需修正为条件概率 P(rank_i ≤ K_max | updated)。

## Corrected Claim

P(rank_i ≤ K_max) 的量化计算：由于 K_max ≈ 98,500 且总对象数 N=100,000，该概率为 98.5%。但在 ρ=-0.3 的负相关下，被更新的对象若为高频小对象，其 rank_i 更可能小于 K_max，需修正为条件概率 P(rank_i ≤ K_max | updated)。

## Evidence

先验知识/题面给定，逻辑校验通过：98,500/100,000=98.5%计算正确，且负相关下高频小对象更可能位于低排名（rank小），故条件概率修正逻辑自洽。
