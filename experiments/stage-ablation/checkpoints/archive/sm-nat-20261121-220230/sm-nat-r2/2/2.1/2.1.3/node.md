# N48: LFU 增益上限受限于热度排名变化率 v：若排名变化率 v > 阈值 v_crit，LFU 的累计频率统计滞后导致其命中率接近 LRU，增益 ΔH → 0；v_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LFU 增益上限受限于热度排名变化率 v：若排名变化率 v > 阈值 v_crit，LFU 的累计频率统计滞后导致其命中率接近 LRU，增益 ΔH → 0；v_crit 可由热度分布的自相关函数估计。

## Corrected Claim

LFU 增益上限受限于热度排名变化率 v：若排名变化率 v > 阈值 v_crit，LFU 的累计频率统计滞后导致其命中率接近 LRU，增益 ΔH → 0；v_crit 可由热度分布的自相关函数估计。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 依赖历史频率，当工作集热度变化率超过临界值时，统计滞后导致其性能退化至 LRU 水平，符合缓存理论直觉。

## Search Query

LFU performance degradation under changing request patterns
