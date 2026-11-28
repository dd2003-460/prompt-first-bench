# N21: 一次性硬件采购成本（CapEx）计算公式：Total_CapEx = Σ(Price_i × Qty_i) + Interconnect_Cost + Peri

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

一次性硬件采购成本（CapEx）计算公式：Total_CapEx = Σ(Price_i × Qty_i) + Interconnect_Cost + Peripheral_Cost (PSU/Cooling/Motherboard升级)，其中 Price_i 为单卡最新市场价（含二手折价率 [待核验]），Interconnect_Cost 为 NVLink/PCIe Switch 费用（单卡为0），Peripheral_Cost 为多卡方案必需的散热与电源升级增量。

## Corrected Claim

一次性硬件采购成本（CapEx）计算公式：Total_CapEx = Σ(Price_i × Qty_i) + Interconnect_Cost + Peripheral_Cost (PSU/Cooling/Motherboard升级)，其中 Price_i 为单卡最新市场价（含二手折价率 [待核验]），Interconnect_Cost 为 NVLink/PCIe Switch 费用（单卡为0），Peripheral_Cost 为多卡方案必需的散热与电源升级增量。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RTX 4090 used price vs RTX 5090 new price 2024
