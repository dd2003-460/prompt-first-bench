# N229: P99 延迟分解模型：P99_latency = T_network + T_transmit + T_processing。其中 T_network 为固定网

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

P99 延迟分解模型：P99_latency = T_network + T_transmit + T_processing。其中 T_network 为固定网络延迟（公有云~20ms，自建~50ms），T_processing 为服务器处理时间（<5ms），T_transmit = s / B_link。需计算在给定 P99 目标 T 下，允许的最大传输时间 T_transmit_max = T - T_network - T_processing。

## Corrected Claim

P99 延迟分解模型：P99_latency = T_network + T_transmit + T_processing。其中 T_network 为固定网络延迟（公有云~20ms，自建~50ms），T_processing 为服务器处理时间（<5ms），T_transmit = s / B_link。需计算在给定 P99 目标 T 下，允许的最大传输时间 T_transmit_max = T - T_network - T_processing。

## Evidence

先验知识/题面给定，逻辑校验通过：延迟分解模型符合网络通信基本物理原理（总延迟=网络+传输+处理），数值量级（公有云20ms/自建50ms/处理<5ms）符合工程常识，公式推导自洽。

## Search Query

CDN latency breakdown network transmission processing time
