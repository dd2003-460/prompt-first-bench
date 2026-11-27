# N6: 缓存容量 C 的归一化阈值：C_norm = 128GB / (N_obj * E[S])，其中 N_obj=100,000，E[S] 由 Pareto(α=1

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存容量 C 的归一化阈值：C_norm = 128GB / (N_obj * E[S])，其中 N_obj=100,000，E[S] 由 Pareto(α=1.1) 的均值公式 E[S] = α*x_min/(α-1) 计算（需设定 x_min，通常取最小对象大小如 1KB 或 10KB 进行敏感性分析）。

## Corrected Claim

缓存容量 C 的归一化阈值：C_norm = 128GB / (N_obj * E[S])，其中 N_obj=100,000，E[S] 由 Pareto(α=1.1) 的均值公式 E[S] = α*x_min/(α-1) 计算（需设定 x_min，通常取最小对象大小如 1KB 或 10KB 进行敏感性分析）。

## Evidence

父节点级核验未通过：有冗余（子节点之间逻辑互斥（针对不同 x_min 取值），覆盖了父节点定义的所有计算步骤和敏感性分析场景，因此正交且完备。然而，子节点 1 和 2 本质上是同一公式在不同参数下的实例，子节点 3 和 4 同理。这种将‘参数变体’拆分为独立节点的做法导致结构冗余，因为它们共享相同的逻辑结构（公式推导），仅数值不同。）
