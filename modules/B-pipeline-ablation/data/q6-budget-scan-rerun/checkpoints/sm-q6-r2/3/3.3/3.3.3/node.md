# N71: 请求大小分布对 P99 延迟的影响机制：大对象（短视频）传输时间 T_transmit = s / B_link。若 s > 阈值 S_threshold（如 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

请求大小分布对 P99 延迟的影响机制：大对象（短视频）传输时间 T_transmit = s / B_link。若 s > 阈值 S_threshold（如 10MB），T_transmit 可能超过 T - T_network，导致 P99 超标。需计算在 s ~ LogNormal 分布下，P(T_transmit > T - T_network) 的概率，并量化该概率对 P99 延迟的贡献。

## Corrected Claim

请求大小分布对 P99 延迟的影响机制：大对象（短视频）传输时间 T_transmit = s / B_link。若 s > 阈值 S_threshold（如 10MB），T_transmit 可能超过 T - T_network，导致 P99 超标。需计算在 s ~ LogNormal 分布下，P(T_transmit > T - T_network) 的概率，并量化该概率对 P99 延迟的贡献。

## Evidence

先验知识/题面给定，逻辑校验通过：传输时间公式 T=s/B 符合物理定义，大对象导致传输时间增加进而影响 P99 延迟的因果机制在逻辑上自洽，且 LogNormal 分布常用于描述文件大小，量级合理。
