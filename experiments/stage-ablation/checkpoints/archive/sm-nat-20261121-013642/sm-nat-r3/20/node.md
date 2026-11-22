# N291: 更新率对 LRU 有效命中率的折扣系数精确计算：f_update = exp(-λ_u * T_res_avg)。基于 N281 修正的 V_total=1.1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

更新率对 LRU 有效命中率的折扣系数精确计算：f_update = exp(-λ_u * T_res_avg)。基于 N281 修正的 V_total=1.1TB 和 C=128GB，缓存周转率 Turnover = R_total / C ≈ 5000GB/day / 128GB ≈ 39.06 /day。平均驻留时间 T_res_avg ≈ 1 / Turnover ≈ 0.0256 days (约 37 分钟)。代入 λ_u=0.01/day，f_update = exp(-0.01 * 0.0256) ≈ 0.99975。折损系数 δ = 1 - f_update ≈ 0.00025，即有效命中率仅需打 0.99975 折，更新惩罚可忽略不计 (<0.1%)。

## Corrected Claim

更新率对 LRU 有效命中率的折扣系数精确计算：f_update = exp(-λ_u * T_res_avg)。基于 N281 修正的 V_total=1.1TB 和 C=128GB，缓存周转率 Turnover = R_total / C ≈ 5000GB/day / 128GB ≈ 39.06 /day。平均驻留时间 T_res_avg ≈ 1 / Turnover ≈ 0.0256 days (约 37 分钟)。代入 λ_u=0.01/day，f_update = exp(-0.01 * 0.0256) ≈ 0.99975。折损系数 δ = 1 - f_update ≈ 0.00025，即有效命中率仅需打 0.99975 折，更新惩罚可忽略不计 (<0.1%)。

## Evidence

检索失败: no sources from any channel (all 5 failed)
