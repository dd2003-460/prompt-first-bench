# N518: TTL=24h 工作点下，因内容更新导致的用户感知“陈旧”请求占比 P_stale 约为 5%-10%，计算公式为 P_stale = (1 - H_dynam

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N167

## Claim

TTL=24h 工作点下，因内容更新导致的用户感知“陈旧”请求占比 P_stale 约为 5%-10%，计算公式为 P_stale = (1 - H_dynamic) * P_update_freq，其中 P_update_freq 为对象在 24h 内被修改的概率，对于非实时内容通常 < 5%。

## Corrected Claim

TTL=24h 工作点下，因内容更新导致的用户感知“陈旧”请求占比 P_stale 约为 5%-10%，计算公式为 P_stale = (1 - H_dynamic) * P_update_freq，其中 P_update_freq 为对象在 24h 内被修改的概率，对于非实时内容通常 < 5%。

## Evidence

先验知识/题面给定，逻辑校验通过
