# N45: LFU 增益 ΔH 的量化上限公式：ΔH ≤ ∫_{s_min}^{s_max} [f_R(r|s)_LFU - f_R(r|s)_LRU] × f_S(s) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

LFU 增益 ΔH 的量化上限公式：ΔH ≤ ∫_{s_min}^{s_max} [f_R(r|s)_LFU - f_R(r|s)_LRU] × f_S(s) ds，其中 f_R(r|s)_LFU 反映 LFU 偏好高频小对象的联合分布偏移，需通过数值积分计算具体百分点

## Corrected Claim

LFU 增益 ΔH 的量化上限公式：ΔH ≤ ∫_{s_min}^{s_max} [f_R(r|s)_LFU - f_R(r|s)_LRU] × f_S(s) ds，其中 f_R(r|s)_LFU 反映 LFU 偏好高频小对象的联合分布偏移，需通过数值积分计算具体百分点

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU hit rate gain formula Pareto request distribution negative correlation size popularity
