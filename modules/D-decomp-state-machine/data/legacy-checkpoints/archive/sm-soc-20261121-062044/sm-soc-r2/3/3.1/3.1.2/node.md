# N55: 强制降价幅度 Δp 的计算：Δp = (P_current - P_target) / P_current，其中 P_target 为近期成交均价，需设定阈值 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15, N16, N17

## Claim

强制降价幅度 Δp 的计算：Δp = (P_current - P_target) / P_current，其中 P_target 为近期成交均价，需设定阈值 Δp_min = 5% 以确保信号显著性，低于此值视为无效干预。

## Corrected Claim

强制降价幅度 Δp 的计算：Δp = (P_current - P_target) / P_current，其中 P_target 为近期成交均价，需设定阈值 Δp_min = 5% 以确保信号显著性，低于此值视为无效干预。

## Evidence

先验知识/题面给定，逻辑校验通过
