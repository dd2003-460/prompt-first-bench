# N334: T_diagnose复杂度因子：多POP故障定位时间T_diagnose = T_single * k_correlation，其中T_single=10min

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

T_diagnose复杂度因子：多POP故障定位时间T_diagnose = T_single * k_correlation，其中T_single=10min，k_correlation∈[1.0, 2.0]（取决于故障共因比例），共因故障（如骨干网中断）增加诊断复杂度

## Corrected Claim

T_diagnose复杂度因子：多POP故障定位时间T_diagnose = T_single * k_correlation，其中T_single=10min，k_correlation∈[1.0, 2.0]（取决于故障共因比例），共因故障（如骨干网中断）增加诊断复杂度

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-POP fault diagnosis complexity correlation factor
