# N200: T_hours 的电力成本敏感性系数：TCO_power = P_avg × T_hours × $kWh，其中 P_avg 为平均功耗（非峰值），若 P_av

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

T_hours 的电力成本敏感性系数：TCO_power = P_avg × T_hours × $kWh，其中 P_avg 为平均功耗（非峰值），若 P_avg 为峰值的 60-70%，则 TCO_power 对 T_hours 的敏感度系数为 1.0（线性关系），即 T_hours 每增加 10%，TCO_power 增加 10%，但 TCO_total 中电力占比约 15-20%，因此 T_hours 每增加 10%，TCO_total 仅增加 1.5-2.0%

## Corrected Claim

T_hours 的电力成本敏感性系数：TCO_power = P_avg × T_hours × $kWh，其中 P_avg 为平均功耗（非峰值），若 P_avg 为峰值的 60-70%，则 TCO_power 对 T_hours 的敏感度系数为 1.0（线性关系），即 T_hours 每增加 10%，TCO_power 增加 10%，但 TCO_total 中电力占比约 15-20%，因此 T_hours 每增加 10%，TCO_total 仅增加 1.5-2.0%

## Evidence

先验知识/题面给定，逻辑校验通过：TCO_power与T_hours呈线性关系（敏感度1.0），TCO_total增量=电力占比(15-20%)×T_hours增量(10%)=1.5-2.0%，数学推导自洽。
