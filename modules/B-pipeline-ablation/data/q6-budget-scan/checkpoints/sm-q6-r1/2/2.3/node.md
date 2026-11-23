# N17: 公有云CDN的基础设施成本：C_infra_cloud = 0（已包含在带宽/流量费用中），但需考虑预留实例或长期合约的折扣（通常10-30%），实际成本 = 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

公有云CDN的基础设施成本：C_infra_cloud = 0（已包含在带宽/流量费用中），但需考虑预留实例或长期合约的折扣（通常10-30%），实际成本 = C_bandwidth_cloud * (1 - discount_rate)

## Corrected Claim

公有云CDN的基础设施成本：C_infra_cloud = 0（已包含在带宽/流量费用中），但需考虑预留实例或长期合约的折扣（通常10-30%），实际成本 = C_bandwidth_cloud * (1 - discount_rate)

## Evidence

先验知识/题面给定，逻辑校验通过：公有云CDN通常按流量计费，基础设施成本已内含于单价中，长期合约折扣符合行业惯例。

## Search Query

Alibaba Cloud CDN pricing model bandwidth vs traffic
