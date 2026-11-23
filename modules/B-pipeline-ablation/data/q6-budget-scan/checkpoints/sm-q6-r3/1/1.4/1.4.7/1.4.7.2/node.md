# N148: 量化公有云突发流量溢价成本：公有云在超出95th峰值部分的突发流量单价 P_burst 通常为常规单价的 1.2-1.5 倍，若突发流量占比为 5%，则额外成本

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

量化公有云突发流量溢价成本：公有云在超出95th峰值部分的突发流量单价 P_burst 通常为常规单价的 1.2-1.5 倍，若突发流量占比为 5%，则额外成本 C_burst_extra = BW_burst * P_bw_base * (P_burst_ratio - 1) * T_burst_duration。

## Corrected Claim

量化公有云突发流量溢价成本：公有云在超出95th峰值部分的突发流量单价 P_burst 通常为常规单价的 1.2-1.5 倍，若突发流量占比为 5%，则额外成本 C_burst_extra = BW_burst * P_bw_base * (P_burst_ratio - 1) * T_burst_duration。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud CDN burst traffic pricing premium 95th percentile
