# N118: ΔH_lock 的精确计算依赖于 LFU 头部锁定率与 LRU 头部保留率的差值乘以头部请求占比：ΔH_lock = (L_LFU_top - L_LRU_to

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

ΔH_lock 的精确计算依赖于 LFU 头部锁定率与 LRU 头部保留率的差值乘以头部请求占比：ΔH_lock = (L_LFU_top - L_LRU_top) * P_req_top；其中 P_req_top 在 Pareto(β=0.9) 下为 0.82（N26），L_LFU_top ≈ 0.75，L_LRU_top ≈ 0.68（N26），故 ΔH_lock = (0.75 - 0.68) * 0.82 ≈ 0.0574 (5.74%)，修正 N44 中 '+3~5%' 的范围，表明在强头部效应下锁定优势显著高于此前估算。

## Corrected Claim

ΔH_lock 的精确计算依赖于 LFU 头部锁定率与 LRU 头部保留率的差值乘以头部请求占比：ΔH_lock = (L_LFU_top - L_LRU_top) * P_req_top；其中 P_req_top 在 Pareto(β=0.9) 下为 0.82（N26），L_LFU_top ≈ 0.75，L_LRU_top ≈ 0.68（N26），故 ΔH_lock = (0.75 - 0.68) * 0.82 ≈ 0.0574 (5.74%)，修正 N44 中 '+3~5%' 的范围，表明在强头部效应下锁定优势显著高于此前估算。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (0.75 - 0.68) * 0.82 = 0.0574 正确，量级合理，符合 LFU 在强头部效应下优于 LRU 的缓存理论直觉。
