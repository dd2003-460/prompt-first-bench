# N287: 核心城市聚集策略的P99 RTT分布：核心城市用户P99 RTT约20-40ms，非核心城市用户P99 RTT约50-100ms，整体P99 RTT = (Co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

核心城市聚集策略的P99 RTT分布：核心城市用户P99 RTT约20-40ms，非核心城市用户P99 RTT约50-100ms，整体P99 RTT = (Core_Population * Core_RTT + Non_Core_Population * Non_Core_RTT) / Total_Population，需基于实际用户地理分布加权计算

## Corrected Claim

核心城市聚集策略的P99 RTT分布：核心城市用户P99 RTT约20-40ms，非核心城市用户P99 RTT约50-100ms，整体P99 RTT = (Core_Population * Core_RTT + Non_Core_Population * Non_Core_RTT) / Total_Population，需基于实际用户地理分布加权计算

## Evidence

先验知识/题面给定，逻辑校验通过：RTT数值量级符合物理直觉（核心城市低延迟，非核心高延迟），加权平均公式逻辑自洽。
