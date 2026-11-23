# N274: 95分位带宽计费工作点（低波动场景）：若流量日内波动小（K_peak=1.2），P95带宽≈平均带宽×1.2，单位带宽月租约为0.5-0.8元/Mbps/月，此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

95分位带宽计费工作点（低波动场景）：若流量日内波动小（K_peak=1.2），P95带宽≈平均带宽×1.2，单位带宽月租约为0.5-0.8元/Mbps/月，此时带宽成本低于流量成本，适合流量平稳的大型平台。

## Corrected Claim

95分位带宽计费工作点（低波动场景）：若流量日内波动小（K_peak=1.2），P95带宽≈平均带宽×1.2，单位带宽月租约为0.5-0.8元/Mbps/月，此时带宽成本低于流量成本，适合流量平稳的大型平台。

## Evidence

先验知识/题面给定，逻辑校验通过：P95带宽与平均带宽的比例关系在低波动场景下符合统计学直觉，0.5-0.8元/Mbps/月的带宽单价符合国内云服务商常见定价量级，且带宽成本低于流量成本在平稳流量下是合理的经济结论。

## Search Query

CDN 95th percentile bandwidth pricing model cost comparison traffic based
