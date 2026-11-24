# N414: 混合策略下，西部长尾流量路由至公有云 CDN 的成本增量 ΔC_bw_tail = R_tail * s_avg * (1 - H_tail) * P_clou

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

混合策略下，西部长尾流量路由至公有云 CDN 的成本增量 ΔC_bw_tail = R_tail * s_avg * (1 - H_tail) * P_cloud_bw - R_tail * s_avg * (1 - H_tail) * P_self_bw，其中 R_tail = 0.05 * R_daily，P_cloud_bw 为公有云西部流量单价（通常比东部高 10-20%），P_self_bw 为自建回源带宽成本。

## Corrected Claim

混合策略下，西部长尾流量路由至公有云 CDN 的成本增量 ΔC_bw_tail = R_tail * s_avg * (1 - H_tail) * P_cloud_bw - R_tail * s_avg * (1 - H_tail) * P_self_bw，其中 R_tail = 0.05 * R_daily，P_cloud_bw 为公有云西部流量单价（通常比东部高 10-20%），P_self_bw 为自建回源带宽成本。

## Evidence

先验知识/题面给定，逻辑校验通过
