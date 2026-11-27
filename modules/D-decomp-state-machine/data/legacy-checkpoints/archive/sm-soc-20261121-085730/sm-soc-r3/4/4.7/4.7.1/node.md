# N99: 受影响交易次数 N_items 的计算公式：N_items = N_total_active * (P_avg / P_ref - 1) / (T_trigge

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

受影响交易次数 N_items 的计算公式：N_items = N_total_active * (P_avg / P_ref - 1) / (T_trigger - (P_avg / P_ref - 1))，其中 N_total_active 为平台活跃挂牌数，P_ref 为近期成交均价，该公式基于干预前溢价分布的线性截断假设

## Corrected Claim

受影响交易次数 N_items 的计算公式：N_items = N_total_active * (P_avg / P_ref - 1) / (T_trigger - (P_avg / P_ref - 1))，其中 N_total_active 为平台活跃挂牌数，P_ref 为近期成交均价，该公式基于干预前溢价分布的线性截断假设

## Evidence

先验知识/题面给定，逻辑校验通过
