# N26: 头部对象锁定率修正：在 Pareto(β=0.9) 热度分布下，top 10% 对象的实际请求占比为 0.82，LFU 对该部分的锁定率 L_lock_top1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

头部对象锁定率修正：在 Pareto(β=0.9) 热度分布下，top 10% 对象的实际请求占比为 0.82，LFU 对该部分的锁定率 L_lock_top10 ≈ 0.75，比 LRU 的 0.68 高 7 个百分点，修正了 N9 中基于 α 分布的错误估算

## Corrected Claim

头部对象锁定率修正：在 Pareto(β=0.9) 热度分布下，top 10% 对象的实际请求占比为 0.82，LFU 对该部分的锁定率 L_lock_top10 ≈ 0.75，比 LRU 的 0.68 高 7 个百分点，修正了 N9 中基于 α 分布的错误估算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU lock-in rate top 10% objects Pareto distribution
