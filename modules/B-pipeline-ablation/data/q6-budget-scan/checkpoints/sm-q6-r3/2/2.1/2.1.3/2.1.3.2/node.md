# N247: 单点机柜数量 N_racks 的确定公式：N_racks = ceil(P_IT_total / P_rack_capacity)，其中 P_IT_total 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

单点机柜数量 N_racks 的确定公式：N_racks = ceil(P_IT_total / P_rack_capacity)，其中 P_IT_total 为单点IT设备总功率（5-10kW），P_rack_capacity 为单柜标准功率上限（通常10kW），故 N_racks ≈ 1-2，若考虑冗余则取2-3

## Corrected Claim

单点机柜数量 N_racks 的确定公式：N_racks = ceil(P_IT_total / P_rack_capacity)，其中 P_IT_total 为单点IT设备总功率（5-10kW），P_rack_capacity 为单柜标准功率上限（通常10kW），故 N_racks ≈ 1-2，若考虑冗余则取2-3

## Evidence

先验知识/题面给定，逻辑校验通过：公式 N_racks = ceil(P_IT_total / P_rack_capacity) 符合工程常识，数值量级（5-10kW IT功率对应1-2柜，冗余后2-3柜）合理且自洽。
