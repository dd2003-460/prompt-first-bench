# N131: 混合策略中边界区域流量切分成本增量：C_boundary_hybrid = P_boundary * Q_total * (P_bw_cloud_boundar

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

混合策略中边界区域流量切分成本增量：C_boundary_hybrid = P_boundary * Q_total * (P_bw_cloud_boundary - P_bw_self_estimated)，其中 P_bw_cloud_boundary 为公有云在偏远地区的单价（通常为国内均价的 1.2-1.5 倍），P_bw_self_estimated 为自建节点分摊到该区域的带宽成本（接近 0 若已覆盖）

## Corrected Claim

混合策略中边界区域流量切分成本增量：C_boundary_hybrid = P_boundary * Q_total * (P_bw_cloud_boundary - P_bw_self_estimated)，其中 P_bw_cloud_boundary 为公有云在偏远地区的单价（通常为国内均价的 1.2-1.5 倍），P_bw_self_estimated 为自建节点分摊到该区域的带宽成本（接近 0 若已覆盖）

## Evidence

先验知识/题面给定，逻辑校验通过
