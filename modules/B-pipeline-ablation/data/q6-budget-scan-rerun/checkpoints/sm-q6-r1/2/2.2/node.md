# N12: 带宽成本（按量/包年）公式：Cost_bandwidth = (日均下载量 2TB × 365 × 带宽单价) / 年请求总量 × 1000；公有云 CDN 单

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

带宽成本（按量/包年）公式：Cost_bandwidth = (日均下载量 2TB × 365 × 带宽单价) / 年请求总量 × 1000；公有云 CDN 单价约为 0.2 元/GB（阶梯定价，日均 2TB 处于较高档位），自建节点需计算骨干网带宽租赁成本（约 0.1 元/GB，但需预付大额带宽包）

## Corrected Claim

带宽成本（按量/包年）公式：Cost_bandwidth = (日均下载量 2TB × 365 × 带宽单价) / 年请求总量 × 1000；公有云 CDN 单价约为 0.2 元/GB（阶梯定价，日均 2TB 处于较高档位），自建节点需计算骨干网带宽租赁成本（约 0.1 元/GB，但需预付大额带宽包）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Cloud CDN bandwidth pricing 0.2 CNY/GB tiered pricing self-hosted backbone bandwidth cost 0.1 CNY/GB
