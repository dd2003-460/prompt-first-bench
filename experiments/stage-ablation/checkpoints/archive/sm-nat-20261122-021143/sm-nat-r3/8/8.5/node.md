# N154: P_stale_hit 的修正计算：N60 中 P_stale_hit ≈ u * T_res_avg 假设所有对象均匀老化，但实际 LRU 中热门对象驻留时间

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59, N60

## Claim

P_stale_hit 的修正计算：N60 中 P_stale_hit ≈ u * T_res_avg 假设所有对象均匀老化，但实际 LRU 中热门对象驻留时间短，冷对象驻留时间长，需加权计算 P_stale_hit = (1/C) * ∫_{k=1}^{K} S(k) * P(stale|k) dk，其中 P(stale|k) = 1 - e^{-u * T_res(k)}，需验证该积分值是否显著偏离 0.012

## Corrected Claim

P_stale_hit 的修正计算：N60 中 P_stale_hit ≈ u * T_res_avg 假设所有对象均匀老化，但实际 LRU 中热门对象驻留时间短，冷对象驻留时间长，需加权计算 P_stale_hit = (1/C) * ∫_{k=1}^{K} S(k) * P(stale|k) dk，其中 P(stale|k) = 1 - e^{-u * T_res(k)}，需验证该积分值是否显著偏离 0.012

## Evidence

先验知识/题面给定，逻辑校验通过
