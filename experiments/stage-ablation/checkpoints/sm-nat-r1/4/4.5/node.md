# N19: 对象更新率 1%/天 对 LRU 有效命中率的影响机制：更新对象在 LRU 中视为冷对象，需重新填充；有效命中率 H_eff = H_LRU * (1 - p_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

对象更新率 1%/天 对 LRU 有效命中率的影响机制：更新对象在 LRU 中视为冷对象，需重新填充；有效命中率 H_eff = H_LRU * (1 - p_update * t_avg)，其中 p_update=0.01/天，t_avg 为对象平均驻留时间；t_avg 可由 LRU 驱逐率推导，t_avg ≈ C / (miss_rate * request_rate * avg_size)，需结合 N6 和 N7 的结果计算，属 knowledge 来源，但 t_avg 的具体值依赖前序计算。

## Corrected Claim

对象更新率 1%/天 对 LRU 有效命中率的影响机制：更新对象在 LRU 中视为冷对象，需重新填充；有效命中率 H_eff = H_LRU * (1 - p_update * t_avg)，其中 p_update=0.01/天，t_avg 为对象平均驻留时间；t_avg 可由 LRU 驱逐率推导，t_avg ≈ C / (miss_rate * request_rate * avg_size)，需结合 N6 和 N7 的结果计算，属 knowledge 来源，但 t_avg 的具体值依赖前序计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU hit rate impact object update rate cache pollution
