# N248: 动态地理分布概率向量 p_i(t) 的构建公式：p_i(t) = (1 - α_mobile) * p_i_static + α_mobile * p_i_ro

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

动态地理分布概率向量 p_i(t) 的构建公式：p_i(t) = (1 - α_mobile) * p_i_static + α_mobile * p_i_roaming，其中 p_i_roaming 为漫游流量在各省的分布概率（通常趋向于热门旅游/商务城市，如京沪广深占比 > 40%）。

## Corrected Claim

动态地理分布概率向量 p_i(t) 的构建公式：p_i(t) = (1 - α_mobile) * p_i_static + α_mobile * p_i_roaming，其中 p_i_roaming 为漫游流量在各省的分布概率（通常趋向于热门旅游/商务城市，如京沪广深占比 > 40%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dynamic user geographic distribution probability vector CDN edge selection
