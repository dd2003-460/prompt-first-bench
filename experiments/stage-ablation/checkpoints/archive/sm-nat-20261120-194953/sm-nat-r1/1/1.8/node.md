# N13: LFU 增益来源：LFU 优先保留高频对象，在 $\beta=0.9$（重尾）下，前 $k\%$ 的对象贡献了 $>50\%$ 的请求，LFU 能更精确地锁定这

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：LFU 基于访问频率，在重尾分布（Zipf-like）下确实能更有效地保留高频头部对象，而 LRU 基于最近访问时间，易受突发冷启动或扫描效应影响，导致高频但非最近访问的对象被驱逐，逻辑自洽且符合缓存替换算法的基本原理。
