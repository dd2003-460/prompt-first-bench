# N12: LFU 相对 LRU 的最大增益百分点：ΔH = H_LFU - H_LRU，由于 LFU 更倾向于保留高频对象，而 LRU 受最近访问影响，在 Pareto 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 相对 LRU 的最大增益百分点：ΔH = H_LFU - H_LRU，由于 LFU 更倾向于保留高频对象，而 LRU 受最近访问影响，在 Pareto 分布下 LFU 能更精确地覆盖热点，增益取决于频率分布的陡峭程度（β=0.9）。

## Corrected Claim

LFU 相对 LRU 的最大增益百分点：ΔH = H_LFU - H_LRU，由于 LFU 更倾向于保留高频对象，而 LRU 受最近访问影响，在 Pareto 分布下 LFU 能更精确地覆盖热点，增益取决于频率分布的陡峭程度（β=0.9）。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU基于频率，LRU基于时间，在Pareto分布（β=0.9）下LFU确实能更精准覆盖热点，逻辑自洽且符合缓存理论常识。

## Search Query

LFU vs LRU performance difference Pareto workload
