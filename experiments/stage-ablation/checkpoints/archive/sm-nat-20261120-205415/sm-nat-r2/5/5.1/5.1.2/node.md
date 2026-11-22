# N67: 工作点2（K=100, β=0.9）：基于前 K 个最热门对象的近似，K=100（缓存容量可容纳对象数），前 100 个对象贡献的流量比例 ≈ 1 - (1/1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

工作点2（K=100, β=0.9）：基于前 K 个最热门对象的近似，K=100（缓存容量可容纳对象数），前 100 个对象贡献的流量比例 ≈ 1 - (1/100)^0.9 ≈ 0.990，即 99.0%，这是基于对象排名的经验上界

## Corrected Claim

工作点2（K=100, β=0.9）：基于前 K 个最热门对象的近似，K=100（缓存容量可容纳对象数），前 100 个对象贡献的流量比例 ≈ 1 - (1/100)^0.9 ≈ 0.990，即 99.0%，这是基于对象排名的经验上界

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - (1/100)^0.9 确实约为 0.990，且符合 Zipf 分布下头部对象流量占比的经验规律。

## Search Query

Pareto distribution top 100 objects traffic contribution beta 0.9
