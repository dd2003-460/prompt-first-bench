# N109: 对象更新率 1%/天 对 LRU 有效命中率的折损系数 D_update 可量化为 D_update ≈ 1 - (λ_update * T_res_avg)，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 1%/天 对 LRU 有效命中率的折损系数 D_update 可量化为 D_update ≈ 1 - (λ_update * T_res_avg)，其中 T_res_avg 为缓存中对象的平均驻留时间。若 T_res_avg = 2 小时（高频对象），则 D_update ≈ 0.9992，折损 0.08%；若 T_res_avg = 24 小时（低频边界对象），则 D_update ≈ 0.99，折损 1%。整体加权折损约为 0.3-0.5%。

## Corrected Claim

对象更新率 1%/天 对 LRU 有效命中率的折损系数 D_update 可量化为 D_update ≈ 1 - (λ_update * T_res_avg)，其中 T_res_avg 为缓存中对象的平均驻留时间。若 T_res_avg = 2 小时（高频对象），则 D_update ≈ 0.9992，折损 0.08%；若 T_res_avg = 24 小时（低频边界对象），则 D_update ≈ 0.99，折损 1%。整体加权折损约为 0.3-0.5%。

## Evidence

检索失败: no sources from any channel (all 5 failed)
