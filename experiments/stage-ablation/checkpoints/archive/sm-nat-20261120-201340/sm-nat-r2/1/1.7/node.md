# N12: 对象大小 Pareto(α=1.1) 的累积分布函数 CDF(s) = (s_min/s)^α，前 k 个最小对象的总大小占比 = 1 - (k/N)^α（近似

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

对象大小 Pareto(α=1.1) 的累积分布函数 CDF(s) = (s_min/s)^α，前 k 个最小对象的总大小占比 = 1 - (k/N)^α（近似，假设对象按大小排序）

## Corrected Claim

对象大小 Pareto(α=1.1) 的累积分布函数 CDF(s) = (s_min/s)^α，前 k 个最小对象的总大小占比 = 1 - (k/N)^α（近似，假设对象按大小排序）

## Evidence

父节点级核验未通过：不完备（父节点核心是CDF公式及其导出的“前k个最小对象总大小占比”这一累积统计量。子节点提供了“截断期望值”公式，这是计算平均大小的工具，但并未直接覆盖父节点中关于“累积占比/总量”的核心推导或结果。虽然截断期望与累积和有关（总量≈k*E[S|S≤s_k]），但子节点仅给出了平均值公式，未明确建立其与父节点中“总大小占比”公式的联系，且缺少对“前k个”这一离散累积过程的直接描述，因此不完备。）

## Search Query

Pareto distribution CDF object size cache
