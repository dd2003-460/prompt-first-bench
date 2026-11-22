# N6: 缓存容量 C=128GB 与工作负载总数据量 W_total 的比值（缓存覆盖率）C/W_total，其中 W_total = 10^5 × E[S]，E[S]

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存容量 C=128GB 与工作负载总数据量 W_total 的比值（缓存覆盖率）C/W_total，其中 W_total = 10^5 × E[S]，E[S] 为 Pareto(α=1.1) 分布的期望大小（需假设最小大小 s_min 以计算 E[S] = α·s_min/(α-1)）

## Corrected Claim

缓存容量 C=128GB 与工作负载总数据量 W_total 的比值（缓存覆盖率）C/W_total，其中 W_total = 10^5 × E[S]，E[S] 为 Pareto(α=1.1) 分布的期望大小（需假设最小大小 s_min 以计算 E[S] = α·s_min/(α-1)）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点严格遵循了从基础参数假设（s_min, E[S]）到中间量计算（W_total），再到最终指标推导（Ratio）的逻辑链条。各步骤之间依赖关系明确，无重复或矛盾，且完整覆盖了父节点定义的所有计算要素。）
