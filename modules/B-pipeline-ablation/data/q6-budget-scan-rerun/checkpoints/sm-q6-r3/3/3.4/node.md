# N19: 请求时间分布与峰值系数：Peak_QPS = Avg_QPS * Peak_Factor，其中Peak_Factor典型值为2-4，影响基础设施容量规划与公有云

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

请求时间分布与峰值系数：Peak_QPS = Avg_QPS * Peak_Factor，其中Peak_Factor典型值为2-4，影响基础设施容量规划与公有云弹性计费成本

## Corrected Claim

请求时间分布与峰值系数：Peak_QPS = Avg_QPS * Peak_Factor，其中Peak_Factor典型值为2-4，影响基础设施容量规划与公有云弹性计费成本

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点与父节点主题严重脱节。父节点关注的是请求时间分布、峰值系数（Peak_Factor）及其对容量规划的影响，属于时间维度和负载波动特性。而子节点讨论的是具体的成本构成（带宽）、存储IOPS（与写入流量相关）、以及缓存命中率（空间/内容维度）。这些子节点并未解释或分解'峰值系数'是如何产生的，也未覆盖'时间分布'这一核心概念。此外，后两个子节点（图片和短视频缓存命中率）本质上是同一参数（缓存命中率）在不同内容类型下的取值，存在冗余。）
