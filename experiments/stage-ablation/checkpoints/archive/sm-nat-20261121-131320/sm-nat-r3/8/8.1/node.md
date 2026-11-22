# N145: 缓存内对象加权平均驻留时间 T_res_avg 的解析推导：T_res_avg = Σ (T_res,i * S_i * f_i) / Σ (S_i * f_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

缓存内对象加权平均驻留时间 T_res_avg 的解析推导：T_res_avg = Σ (T_res,i * S_i * f_i) / Σ (S_i * f_i)，其中 T_res,i 是对象 i 在 LRU 栈中的平均停留时间，对于排名为 i 的对象，T_res,i ≈ 1 / (R * f_i) * (1 - H_i)，该公式将 T_res_avg 与请求率 R 和局部命中率 H_i 关联。

## Corrected Claim

缓存内对象加权平均驻留时间 T_res_avg 的解析推导：T_res_avg = Σ (T_res,i * S_i * f_i) / Σ (S_i * f_i)，其中 T_res,i 是对象 i 在 LRU 栈中的平均停留时间，对于排名为 i 的对象，T_res,i ≈ 1 / (R * f_i) * (1 - H_i)，该公式将 T_res_avg 与请求率 R 和局部命中率 H_i 关联。

## Evidence

先验知识/题面给定，逻辑校验通过
