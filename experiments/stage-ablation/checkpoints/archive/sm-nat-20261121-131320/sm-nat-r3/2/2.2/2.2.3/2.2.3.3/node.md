# N105: 缓存平均填充时间 T_fill 的估算：T_fill = C / (Byte_Inflow_Rate)，其中 Byte_Inflow_Rate = (1 - H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

缓存平均填充时间 T_fill 的估算：T_fill = C / (Byte_Inflow_Rate)，其中 Byte_Inflow_Rate = (1 - H_LRU_static) * Total_Bytes / Day；该值代表缓存被新对象填满一次所需的时间，是触发驱逐事件的时间尺度，直接决定 Jitter_Penalty 的波动周期。

## Corrected Claim

缓存平均填充时间 T_fill 的估算：T_fill = C / (Byte_Inflow_Rate)，其中 Byte_Inflow_Rate = (1 - H_LRU_static) * Total_Bytes / Day；该值代表缓存被新对象填满一次所需的时间，是触发驱逐事件的时间尺度，直接决定 Jitter_Penalty 的波动周期。

## Evidence

先验知识/题面给定，逻辑校验通过：T_fill = 总容量 / 净流入速率，其中净流入速率由未命中流量决定，符合缓存填充的基本物理/逻辑定义。
