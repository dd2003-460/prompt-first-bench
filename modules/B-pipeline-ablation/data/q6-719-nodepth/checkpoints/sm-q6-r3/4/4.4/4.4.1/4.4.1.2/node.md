# N288: IDS_Sensor_License = Bandwidth_GBps × License_Unit_Price_GBps_Month，其中 Bandwidth

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

IDS_Sensor_License = Bandwidth_GBps × License_Unit_Price_GBps_Month，其中 Bandwidth_GBps = Single_POP_Peak_Bandwidth_Mbps / 1000，License_Unit_Price 通常为 ¥500-2000/GBps/月，取决于是否包含威胁情报订阅及分析深度。

## Corrected Claim

IDS_Sensor_License = Bandwidth_GBps × License_Unit_Price_GBps_Month，其中 Bandwidth_GBps = Single_POP_Peak_Bandwidth_Mbps / 1000，License_Unit_Price 通常为 ¥500-2000/GBps/月，取决于是否包含威胁情报订阅及分析深度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

network IDS sensor license cost per Gbps monthly
