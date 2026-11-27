# N13: LFU 增益来源：LFU 优先保留高频对象，在 $\beta=0.9$（重尾）下，前 $k\%$ 的对象贡献了 $>50\%$ 的请求，LFU 能更精确地锁定这

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LFU 增益来源：LFU 优先保留高频对象，在 $\beta=0.9$（重尾）下，前 $k\%$ 的对象贡献了 $>50\%$ 的请求，LFU 能更精确地锁定这些头部对象，而 LRU 易受突发冷启动影响。

## Corrected Claim

LFU 增益来源：LFU 优先保留高频对象，在 $\beta=0.9$（重尾）下，前 $k\%$ 的对象贡献了 $>50\%$ 的请求，LFU 能更精确地锁定这些头部对象，而 LRU 易受突发冷启动影响。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了父节点中关于“重尾分布下头部对象集中度”的数学基础部分，遗漏了父节点中提到的“LRU 易受突发冷启动影响”这一关键机制对比，导致对 LFU 增益来源的解释不完备。）
