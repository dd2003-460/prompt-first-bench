# N122: Energy_Cost 的动态计算：Energy_Cost = Power_Watt * Time_Hours * Price_Per_kWh，其中 Power

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Energy_Cost 的动态计算：Energy_Cost = Power_Watt * Time_Hours * Price_Per_kWh，其中 Power_Watt 非恒定 1.2kW，而是随负载波动；在推理密集阶段（GPU 利用率 >80%）功耗约为 1.1kW，在空闲/检索阶段（GPU 利用率 <20%）功耗约为 0.3kW，需按时间加权平均计算。

## Corrected Claim

Energy_Cost 的动态计算：Energy_Cost = Power_Watt * Time_Hours * Price_Per_kWh，其中 Power_Watt 非恒定 1.2kW，而是随负载波动；在推理密集阶段（GPU 利用率 >80%）功耗约为 1.1kW，在空闲/检索阶段（GPU 利用率 <20%）功耗约为 0.3kW，需按时间加权平均计算。

## Evidence

先验知识/题面给定，逻辑校验通过
