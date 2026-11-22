# N100: 高挂价匹配概率 p_match 的具体计算公式为 p_match = 1 - F_U(P_ask)，其中 F_U 为保留价格 U_i 的累积分布函数（CDF），

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

高挂价匹配概率 p_match 的具体计算公式为 p_match = 1 - F_U(P_ask)，其中 F_U 为保留价格 U_i 的累积分布函数（CDF），当 P_ask 位于第80-90百分位时，p_match 的理论值为 0.1-0.2。

## Corrected Claim

高挂价匹配概率 p_match 的具体计算公式为 p_match = 1 - F_U(P_ask)，其中 F_U 为保留价格 U_i 的累积分布函数（CDF），当 P_ask 位于第80-90百分位时，p_match 的理论值为 0.1-0.2。

## Evidence

先验知识/题面给定，逻辑校验通过：p_match = 1 - F_U(P_ask) 符合定义，若 P_ask 位于第80-90百分位，则 F_U(P_ask) 在 0.8-0.9 之间，故 p_match 在 0.1-0.2 之间，数学推导自洽。
