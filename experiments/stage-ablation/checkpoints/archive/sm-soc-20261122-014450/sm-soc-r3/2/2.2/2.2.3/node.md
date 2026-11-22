# N54: 48小时无咨询的阈值条件：当 ΔQ_consult < 0 时，需满足 β * (P_drop / P_initial) > (V_buyer - P_drop

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

48小时无咨询的阈值条件：当 ΔQ_consult < 0 时，需满足 β * (P_drop / P_initial) > (V_buyer - P_drop) / C_search，其中 V_buyer 为买家估值中位数，C_search 为搜索成本；需计算在 P_drop = 0.9 * P_initial 时，满足该条件的买家比例是否 > 60%，以验证平台数据的合理性。

## Corrected Claim

48小时无咨询的阈值条件：当 ΔQ_consult < 0 时，需满足 β * (P_drop / P_initial) > (V_buyer - P_drop) / C_search，其中 V_buyer 为买家估值中位数，C_search 为搜索成本；需计算在 P_drop = 0.9 * P_initial 时，满足该条件的买家比例是否 > 60%，以验证平台数据的合理性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price drop consultation threshold buyer behavior second hand platform
