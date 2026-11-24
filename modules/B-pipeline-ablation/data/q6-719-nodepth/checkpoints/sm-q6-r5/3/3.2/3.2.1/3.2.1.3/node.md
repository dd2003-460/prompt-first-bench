# N219: 公有云实际出网流量 Traffic_out_cloud = 2,000,000 MB/day * (1 - 0.90) = 200,000 MB/day = 2

- **status**: pending
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

公有云实际出网流量 Traffic_out_cloud = 2,000,000 MB/day * (1 - 0.90) = 200,000 MB/day = 200 GB/day，这是计算公有云带宽成本的基础流量基数。

## Corrected Claim

公有云实际出网流量 Traffic_out_cloud = 2,000,000 MB/day * (1 - 0.90) = 200,000 MB/day = 200 GB/day，这是计算公有云带宽成本的基础流量基数。

## Evidence

父节点级核验未通过：不完备（子节点分别针对‘敏感性分析’和‘峰值修正’两个不同维度，彼此正且不重复。但父节点定义的是‘实际出网流量’这一基础流量基数，子节点仅覆盖了其动态变化（敏感性）和时空分布特性（峰值），未覆盖静态基础参数的来源或验证（如总流量 2,000,000 MB/day 的构成、命中率 0.90 的基准依据等），导致对‘基础流量基数’这一核心概念的分解不完备。）
