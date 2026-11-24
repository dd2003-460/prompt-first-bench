# N31: 用户地理分布的黑盒参数化机制：用户地理分布定义为各区域流量占比 geo_share_i，i=1..N_regions，需通过敏感性分析确定 geo_share_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

用户地理分布的黑盒参数化机制：用户地理分布定义为各区域流量占比 geo_share_i，i=1..N_regions，需通过敏感性分析确定 geo_share_i 的取值范围，典型值为均匀分布（1/N_regions）或 Zipf 分布（geo_share_i ∝ 1/i^α，α=1.0–1.5），地理分布对 CDN 节点部署的影响函数为 C_geo(geo_share) = Σ_i (B_avg × geo_share_i × unit_cost_per_Mbps_i)，不同地理分布下，核心区域和长尾区域的流量权重 w_core 和 w_tail 随之变化。

## Corrected Claim

用户地理分布的黑盒参数化机制：用户地理分布定义为各区域流量占比 geo_share_i，i=1..N_regions，需通过敏感性分析确定 geo_share_i 的取值范围，典型值为均匀分布（1/N_regions）或 Zipf 分布（geo_share_i ∝ 1/i^α，α=1.0–1.5），地理分布对 CDN 节点部署的影响函数为 C_geo(geo_share) = Σ_i (B_avg × geo_share_i × unit_cost_per_Mbps_i)，不同地理分布下，核心区域和长尾区域的流量权重 w_core 和 w_tail 随之变化。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

user geographic distribution traffic share Zipf distribution CDN node deployment cost sensitivity
