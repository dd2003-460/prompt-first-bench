# N133: 当 K > N 时，Pareto 累积分布公式 1 - (K/N)^(1-β) 失效的数学边界：公式仅在 K ≤ N 且 K 为整数时成立；当 K ≥ N 时，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

当 K > N 时，Pareto 累积分布公式 1 - (K/N)^(1-β) 失效的数学边界：公式仅在 K ≤ N 且 K 为整数时成立；当 K ≥ N 时，Top-K 覆盖所有对象，H_req = 100%，此时需切换至‘全量缓存’模型，命中率不再由 Pareto 尾部决定，而由对象失效率决定。

## Corrected Claim

当 K > N 时，Pareto 累积分布公式 1 - (K/N)^(1-β) 失效的数学边界：公式仅在 K ≤ N 且 K 为整数时成立；当 K ≥ N 时，Top-K 覆盖所有对象，H_req = 100%，此时需切换至‘全量缓存’模型，命中率不再由 Pareto 尾部决定，而由对象失效率决定。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto累积分布函数在K>N时数学上无定义或超出范围，Top-K覆盖所有对象时命中率由全量缓存模型决定，符合基本逻辑。
