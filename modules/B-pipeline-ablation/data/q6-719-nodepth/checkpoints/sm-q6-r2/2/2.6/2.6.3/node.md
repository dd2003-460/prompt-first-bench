# N86: 混合策略下长尾区域日均下载流量 (V_tail, GB) 计算为 2000GB * (1 - P_core)，其中 P_core 为核心区域流量占比（由用户地理

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

混合策略下长尾区域日均下载流量 (V_tail, GB) 计算为 2000GB * (1 - P_core)，其中 P_core 为核心区域流量占比（由用户地理分布决定）。

## Corrected Claim

混合策略下长尾区域日均下载流量 (V_tail, GB) 计算为 2000GB * (1 - P_core)，其中 P_core 为核心区域流量占比（由用户地理分布决定）。

## Evidence

先验知识/题面给定，逻辑校验通过：总流量减去核心区域流量即为长尾区域流量，公式 V_tail = Total * (1 - P_core) 在数学上自洽且量纲正确。
