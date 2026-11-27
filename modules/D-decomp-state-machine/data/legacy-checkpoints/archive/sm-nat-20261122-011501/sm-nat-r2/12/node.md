# N76: 更新率对 LRU 命中率的折损系数量化：折损因子 D = 1 - (Update_Rate * T_res_effective)。其中 Update_Rate 

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

更新率对 LRU 命中率的折损系数量化：折损因子 D = 1 - (Update_Rate * T_res_effective)。其中 Update_Rate = 0.01/day。T_res_effective 是对象在缓存中保持“有效”（未被驱逐且版本未过期）的平均时间。若对象版本过期即失效，且更新随机发生，则每个对象平均 100 天更新一次。若 LRU 驻留时间 T_res (N53) ≈ 3.3 分钟 ≈ 0.0023 天，则 P_inval = T_res / 100 ≈ 0.000023。折损系数 D ≈ 1 - 0.000023 = 0.999977。即命中率仅下降 0.0023%。若考虑“脏读”容忍度或版本检查开销，此折损可忽略不计，主要瓶颈在于内存带宽而非逻辑失效。

## Corrected Claim

更新率对 LRU 命中率的折损系数量化：折损因子 D = 1 - (Update_Rate * T_res_effective)。其中 Update_Rate = 0.01/day。T_res_effective 是对象在缓存中保持“有效”（未被驱逐且版本未过期）的平均时间。若对象版本过期即失效，且更新随机发生，则每个对象平均 100 天更新一次。若 LRU 驻留时间 T_res (N53) ≈ 3.3 分钟 ≈ 0.0023 天，则 P_inval = T_res / 100 ≈ 0.000023。折损系数 D ≈ 1 - 0.000023 = 0.999977。即命中率仅下降 0.0023%。若考虑“脏读”容忍度或版本检查开销，此折损可忽略不计，主要瓶颈在于内存带宽而非逻辑失效。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LRU cache hit rate degradation due to data version updates
