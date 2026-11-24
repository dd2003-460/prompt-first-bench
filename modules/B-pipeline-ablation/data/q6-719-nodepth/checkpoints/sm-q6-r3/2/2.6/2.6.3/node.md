# N86: 混合策略下长尾区域日均下载流量 (V_tail, GB) 计算为 2000GB * (1 - P_core)，其中 P_core 为核心区域流量占比（由用户地理

- **status**: pending
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

父节点级核验未通过：不完备（子节点之间存在逻辑依赖而非正交（子节点2依赖子节点1的值），且未覆盖父节点公式中'总流量2000GB'这一关键输入参数的来源或定义，导致完备性不足。）
