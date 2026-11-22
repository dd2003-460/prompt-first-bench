# N7: 访问频率的截断 Pareto 分布参数：请求热度服从 Pareto(β=0.9, f_min)，需确定 f_min 使得总请求量为 5000 万次/天，即 su

- **status**: pending
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

访问频率的截断 Pareto 分布参数：请求热度服从 Pareto(β=0.9, f_min)，需确定 f_min 使得总请求量为 5000 万次/天，即 sum(f_i) = 50,000,000，从而确定每个对象的平均访问频率。

## Corrected Claim

访问频率的截断 Pareto 分布参数：请求热度服从 Pareto(β=0.9, f_min)，需确定 f_min 使得总请求量为 5000 万次/天，即 sum(f_i) = 50,000,000，从而确定每个对象的平均访问频率。

## Evidence

父节点级核验未通过：不完备（子节点存在严重的数学公式错误，导致推导结果无效；且未覆盖父节点中‘确定每个对象的具体访问频率分布’这一核心目标，仅计算了最小频率和头部占比。）
