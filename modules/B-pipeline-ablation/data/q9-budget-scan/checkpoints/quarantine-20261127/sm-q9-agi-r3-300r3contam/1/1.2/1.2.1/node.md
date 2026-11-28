# N34: 27b模型在CoT推理中，单步逻辑正确率p_step约为0.9-0.95，累积错误率E_cumulative(N) = 1 - p_step^N，当N=15时E

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

27b模型在CoT推理中，单步逻辑正确率p_step约为0.9-0.95，累积错误率E_cumulative(N) = 1 - p_step^N，当N=15时E_cumulative约为22.5%-46.4%，表明15步是可靠的迭代深度上限。

## Corrected Claim

27b模型在CoT推理中，单步逻辑正确率p_step约为0.9-0.95，累积错误率E_cumulative(N) = 1 - p_step^N，当N=15时E_cumulative约为22.5%-46.4%，表明15步是可靠的迭代深度上限。

## Evidence

父节点级核验未通过：有冗余（子节点实质上是同一公式 E_cumulative = 1 - p_step^N 在不同参数 (N, p_step) 下的具体实例化，属于‘参数扫描’而非概念上的独立正交维度；此外，子节点C中引用的‘N55’未在父节点或上下文中定义，存在信息缺失风险。）
