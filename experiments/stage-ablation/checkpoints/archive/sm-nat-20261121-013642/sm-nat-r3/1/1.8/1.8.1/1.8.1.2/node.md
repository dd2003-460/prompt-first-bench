# N159: 工作点2（过渡区）：当 T_residence ≈ 100 天时，P_updated_in_cache = 0.01 * 100 = 1.0，但实际受限于缓存中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点2（过渡区）：当 T_residence ≈ 100 天时，P_updated_in_cache = 0.01 * 100 = 1.0，但实际受限于缓存中对象总数，需使用精确公式 P = 1 - exp(-0.01 * T_residence) ≈ 0.632

## Corrected Claim

工作点2（过渡区）：当 T_residence ≈ 100 天时，P_updated_in_cache = 0.01 * 100 = 1.0，但实际受限于缓存中对象总数，需使用精确公式 P = 1 - exp(-0.01 * T_residence) ≈ 0.632

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程/指数分布中，事件发生概率 P = 1 - exp(-λt)，当 λt=1 时 P≈0.632，且线性近似 1.0 在 t 较大时确实高估概率，逻辑自洽。
