# N105: 带宽峰值计费模式成本公式：若采用按带宽峰值计费，Cost_bw_peak = P_bw_peak × B_peak_max × T_month，其中 B_pea

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

带宽峰值计费模式成本公式：若采用按带宽峰值计费，Cost_bw_peak = P_bw_peak × B_peak_max × T_month，其中 B_peak_max 为月内最大带宽峰值（Gbps），P_bw_peak 为每 Gbps 月单价（¥1000-3000/Gbps/月）；对于 2TB/天平均流量，平均带宽 23.1Gbps，峰值 69.3Gbps，需对比流量计费与带宽计费两种模式的月度总成本。

## Corrected Claim

带宽峰值计费模式成本公式：若采用按带宽峰值计费，Cost_bw_peak = P_bw_peak × B_peak_max × T_month，其中 B_peak_max 为月内最大带宽峰值（Gbps），P_bw_peak 为每 Gbps 月单价（¥1000-3000/Gbps/月）；对于 2TB/天平均流量，平均带宽 23.1Gbps，峰值 69.3Gbps，需对比流量计费与带宽计费两种模式的月度总成本。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/天流量换算为平均带宽23.1Gbps（2*1024*1024*1024*8/86400≈23.15Gbps），峰值3倍即69.3Gbps，量级与公式逻辑自洽。
