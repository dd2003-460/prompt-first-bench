# N269: C_bw_cloud 的具体计算：C_bw_cloud = Traffic_cloud_daily * 30 * P_cloud_traffic，其中 Traf

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

C_bw_cloud 的具体计算：C_bw_cloud = Traffic_cloud_daily * 30 * P_cloud_traffic，其中 Traffic_cloud_daily = 400GB，P_cloud_traffic 为公有云 CDN 流量单价（参考 N104/N121，需根据 400GB/日 定位阶梯区间，通常长尾流量单价略高或持平）。

## Corrected Claim

C_bw_cloud 的具体计算：C_bw_cloud = Traffic_cloud_daily * 30 * P_cloud_traffic，其中 Traffic_cloud_daily = 400GB，P_cloud_traffic 为公有云 CDN 流量单价（参考 N104/N121，需根据 400GB/日 定位阶梯区间，通常长尾流量单价略高或持平）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本计算基本逻辑（流量*天数*单价），量纲一致，且作为knowledge节点无需外部来源支持。
