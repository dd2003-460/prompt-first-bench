# N182: 回源链路服务时间 $T_{service}$ 由对象传输时间和源站处理时间组成：$T_{service} = s_{backhaul}/B_{link} + T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

回源链路服务时间 $T_{service}$ 由对象传输时间和源站处理时间组成：$T_{service} = s_{backhaul}/B_{link} + T_{proc}$，其中 $s_{backhaul}$ 为回源对象平均大小，$B_{link}$ 为回源带宽（通常受限于源站出口或骨干网带宽），$T_{proc}$ 为源站服务器处理延迟（典型值 5-20ms）。

## Corrected Claim

回源链路服务时间 $T_{service}$ 由对象传输时间和源站处理时间组成：$T_{service} = s_{backhaul}/B_{link} + T_{proc}$，其中 $s_{backhaul}$ 为回源对象平均大小，$B_{link}$ 为回源带宽（通常受限于源站出口或骨干网带宽），$T_{proc}$ 为源站服务器处理延迟（典型值 5-20ms）。

## Evidence

先验知识/题面给定，逻辑校验通过：回源服务时间由传输时间（大小/带宽）和处理时间组成符合网络通信基本模型，典型处理延迟5-20ms在工程实践中合理。
