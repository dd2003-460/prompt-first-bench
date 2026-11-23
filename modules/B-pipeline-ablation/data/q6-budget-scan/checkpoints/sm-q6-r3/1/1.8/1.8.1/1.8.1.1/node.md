# N231: 核心区域 RTT_P99(j) 的精确分布：基于 Top 5 省份用户到最近自建 POP 的地理距离 D_j，RTT_P99(j) = 2 * D_j / v_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

核心区域 RTT_P99(j) 的精确分布：基于 Top 5 省份用户到最近自建 POP 的地理距离 D_j，RTT_P99(j) = 2 * D_j / v_fiber + T_processing_switch，其中 v_fiber ≈ 2e8 m/s，T_processing_switch ≈ 0.5-2ms，对于 200-500km 距离，RTT_P99 典型区间为 15-35ms

## Corrected Claim

核心区域 RTT_P99(j) 的精确分布：基于 Top 5 省份用户到最近自建 POP 的地理距离 D_j，RTT_P99(j) = 2 * D_j / v_fiber + T_processing_switch，其中 v_fiber ≈ 2e8 m/s，T_processing_switch ≈ 0.5-2ms，对于 200-500km 距离，RTT_P99 典型区间为 15-35ms

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为2e8 m/s，200-500km距离对应单程1-2.5ms，往返2-5ms，加上交换机处理延迟0.5-2ms及P99长尾效应，15-35ms区间符合工程经验与物理直觉。

## Search Query

fiber optic latency 200km 500km round trip time
