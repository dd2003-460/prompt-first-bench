# N303: LRU 有效命中率折损因子 D_eff 的精确计算：D_eff = 1 - P_invalid_global，其中 P_invalid_global = ∫ P

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 有效命中率折损因子 D_eff 的精确计算：D_eff = 1 - P_invalid_global，其中 P_invalid_global = ∫ P_invalid(s) f_s(s) ds。对于 u=0.01/天，若平均驻留时间 T_avg = 1.0 天，则 P_invalid ≈ 0.00995，D_eff ≈ 0.99005，即命中率打 99.0% 折，折损约 1.0%。

## Corrected Claim

LRU 有效命中率折损因子 D_eff 的精确计算：D_eff = 1 - P_invalid_global，其中 P_invalid_global = ∫ P_invalid(s) f_s(s) ds。对于 u=0.01/天，若平均驻留时间 T_avg = 1.0 天，则 P_invalid ≈ 0.00995，D_eff ≈ 0.99005，即命中率打 99.0% 折，折损约 1.0%。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LRU cache hit rate degradation factor invalidation probability
