# N267: C_bw_self 的具体计算：C_bw_self = B_peak_self * P_bw_self * 30，其中 B_peak_self 为核心区域峰值带

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

C_bw_self 的具体计算：C_bw_self = B_peak_self * P_bw_self * 30，其中 B_peak_self 为核心区域峰值带宽（需根据 1.6TB/日 及峰值系数 K_peak 估算），P_bw_self 为自建节点出网带宽单价（通常低于公有云，但需包含专线/公网成本）。

## Corrected Claim

C_bw_self 的具体计算：C_bw_self = B_peak_self * P_bw_self * 30，其中 B_peak_self 为核心区域峰值带宽（需根据 1.6TB/日 及峰值系数 K_peak 估算），P_bw_self 为自建节点出网带宽单价（通常低于公有云，但需包含专线/公网成本）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

self-hosted CDN bandwidth cost vs cloud egress fee
