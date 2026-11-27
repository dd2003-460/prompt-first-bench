# N48: LFU 增益上限受限于热度排名变化率 v：若排名变化率 v > 阈值 v_crit，LFU 的累计频率统计滞后导致其命中率接近 LRU，增益 ΔH → 0；v_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LFU 增益上限受限于热度排名变化率 v：若排名变化率 v > 阈值 v_crit，LFU 的累计频率统计滞后导致其命中率接近 LRU，增益 ΔH → 0；v_crit 可由热度分布的自相关函数估计。

## Corrected Claim

LFU 增益上限受限于热度排名变化率 v：若排名变化率 v > 阈值 v_crit，LFU 的累计频率统计滞后导致其命中率接近 LRU，增益 ΔH → 0；v_crit 可由热度分布的自相关函数估计。

## Evidence

父节点级核验未通过：有冗余（子节点分别描述了低、中、高波动三种特定工作点下的具体数值表现，彼此之间在参数取值上互斥，无矛盾（正交）。它们共同覆盖了从增益显著到增益消失的完整光谱，且隐含了 v_crit 的存在（完备）。然而，这三个子节点本质上是同一物理规律（LFU 增益随 v 变化）在不同参数值下的实例化，属于典型的‘参数扫描’冗余，而非结构性分解。）

## Search Query

LFU performance degradation under changing request patterns
