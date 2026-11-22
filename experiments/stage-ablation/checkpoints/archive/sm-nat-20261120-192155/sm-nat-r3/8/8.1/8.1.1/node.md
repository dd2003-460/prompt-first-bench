# N126: 对象i在LRU缓存中的更新驱逐概率p_evict_i的简化形式为p_evict_i ≈ T_res_i / T_upd_i，其中T_res_i为对象i的驻留时间

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

对象i在LRU缓存中的更新驱逐概率p_evict_i的简化形式为p_evict_i ≈ T_res_i / T_upd_i，其中T_res_i为对象i的驻留时间，T_upd_i = 1 / (U * f_i)为对象i的平均更新间隔，U=0.01/day为全局更新率，f_i = r_i / R_total为对象i的访问频率占比。

## Corrected Claim

对象i在LRU缓存中的更新驱逐概率p_evict_i的简化形式为p_evict_i ≈ T_res_i / T_upd_i，其中T_res_i为对象i的驻留时间，T_upd_i = 1 / (U * f_i)为对象i的平均更新间隔，U=0.01/day为全局更新率，f_i = r_i / R_total为对象i的访问频率占比。

## Evidence

先验知识/题面给定，逻辑校验通过：在LRU缓存中，若对象更新视为驱逐事件，则驱逐概率近似等于驻留时间与更新间隔之比，量纲与逻辑自洽。
