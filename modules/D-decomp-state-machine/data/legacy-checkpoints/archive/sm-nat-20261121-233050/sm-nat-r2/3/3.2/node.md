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

父节点级核验未通过：不完备（子节点存在逻辑覆盖缺失。父节点核心在于解释‘增益取决于频率分布陡峭程度’，但子节点1讨论的是边界情况（M/C=1.0，增益为0），子节点2讨论的是通用机制（M/C<1.0），两者虽然正交且不冗余，但均未直接回应‘为何β=0.9会导致特定增益’这一因果链条。父节点强调β的影响，而子节点未分解出‘频率分布形状（β）如何量化影响ΔH’这一关键方面，仅给出了机制和边界值，导致对‘取决于频率分布陡峭程度’的解释不完整。）

## Search Query

LFU vs LRU performance difference Pareto workload
