# N12: LFU 相对 LRU 的最大增益百分点：ΔH = H_LFU - H_LRU，由于 LFU 更倾向于保留高频对象，而 LRU 受最近访问影响，在 Pareto 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 相对 LRU 的最大增益百分点：ΔH = H_LFU - H_LRU，由于 LFU 更倾向于保留高频对象，而 LRU 受最近访问影响，在 Pareto 分布下 LFU 能更精确地覆盖热点，增益取决于频率分布的陡峭程度（β=0.9）。

## Corrected Claim

LFU 相对 LRU 的最大增益百分点：ΔH = H_LFU - H_LRU，由于 LFU 更倾向于保留高频对象，而 LRU 受最近访问影响，在 Pareto 分布下 LFU 能更精确地覆盖热点，增益取决于频率分布的陡峭程度（β=0.9）。

## Evidence

父节点级核验未通过：不完备（子节点1讨论的是 M/C=1.0 的边界情况（增益为0），子节点2讨论的是 M/C<1.0 的一般机制（增益来源）。两者在逻辑上正交（互斥的工作点条件），且没有重复。但是，父节点明确提到了增益取决于频率分布的陡峭程度（β=0.9），而子节点2仅给出了一个基于字节和频率的近似公式，未显式涵盖或解释 β 参数如何具体影响该增益（例如通过 Zipf 分布推导 miss rate 的变化），导致对父节点中“取决于β”这一关键约束的覆盖不完备。）

## Search Query

LFU vs LRU performance difference Pareto workload
