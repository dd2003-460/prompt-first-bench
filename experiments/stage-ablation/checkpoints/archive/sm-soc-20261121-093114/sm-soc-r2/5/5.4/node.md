# N25: 归因结论置信度：‘平台驱动均衡’的归因基于平台算法推荐机制对挂价分布的影响，量化为平台推荐权重 W_rec 与挂价偏差的皮尔逊相关系数 r，若 r > 0.7 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

归因结论置信度：‘平台驱动均衡’的归因基于平台算法推荐机制对挂价分布的影响，量化为平台推荐权重 W_rec 与挂价偏差的皮尔逊相关系数 r，若 r > 0.7 则归因置信度高，否则需考虑卖家个体异质性。

## Corrected Claim

归因结论置信度：‘平台驱动均衡’的归因基于平台算法推荐机制对挂价分布的影响，量化为平台推荐权重 W_rec 与挂价偏差的皮尔逊相关系数 r，若 r > 0.7 则归因置信度高，否则需考虑卖家个体异质性。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于方差分解以量化卖家异质性噪声（统计层面），子节点2聚焦于因果识别策略以排除反向因果（因果层面）。两者分别对应父节点中“否则需考虑卖家个体异质性”和隐含的“归因需基于因果而非仅相关”的逻辑分支，维度不同（统计噪声 vs 因果偏差），无重复且互补。）

## Search Query

correlation platform recommendation weight listing price bias marketplace
