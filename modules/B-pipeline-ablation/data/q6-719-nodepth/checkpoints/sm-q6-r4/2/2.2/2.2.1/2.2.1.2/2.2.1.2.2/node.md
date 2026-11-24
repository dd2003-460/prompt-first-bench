# N617: 超出基础电力包部分的超额电费计算公式为：Excess_Cost = max(0, Actual_Power_kW - Base_Power_kW) × 720h

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N212, N213, N214

## Claim

超出基础电力包部分的超额电费计算公式为：Excess_Cost = max(0, Actual_Power_kW - Base_Power_kW) × 720h × Unit_Price_kWh，其中Unit_Price_kWh通常为¥0.8-1.2/kWh（商业电价+IDC加价），若实际功耗750W且基础包2kW，则Excess_Cost = 0。

## Corrected Claim

超出基础电力包部分的超额电费计算公式为：Excess_Cost = max(0, Actual_Power_kW - Base_Power_kW) × 720h × Unit_Price_kWh，其中Unit_Price_kWh通常为¥0.8-1.2/kWh（商业电价+IDC加价），若实际功耗750W且基础包2kW，则Excess_Cost = 0。

## Evidence

先验知识/题面给定，逻辑校验通过：公式逻辑自洽，750W < 2kW 故超额为0，电价量级符合商业/IDC常识。

## Search Query

IDC excess power cost calculation formula over base package
