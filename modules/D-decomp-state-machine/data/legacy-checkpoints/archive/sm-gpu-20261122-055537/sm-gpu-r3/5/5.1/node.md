# N24: 性价比指标定义：Cost_Efficiency = C_total / (Q_score * T_throughput)，其中 C_total 为 N4 计算的

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

性价比指标定义：Cost_Efficiency = C_total / (Q_score * T_throughput)，其中 C_total 为 N4 计算的 TCO，Q_score 为精度损失调整后的质量得分(0-1)，T_throughput 为 tokens/s。该指标将延迟(性能变量)转化为吞吐量，与成本和质量挂钩。

## Corrected Claim

性价比指标定义：Cost_Efficiency = C_total / (Q_score * T_throughput)，其中 C_total 为 N4 计算的 TCO，Q_score 为精度损失调整后的质量得分(0-1)，T_throughput 为 tokens/s。该指标将延迟(性能变量)转化为吞吐量，与成本和质量挂钩。

## Evidence

父节点级核验未通过：不完备（子节点分别定义了公式中的 Q_score 和 T_throughput，两者概念独立且无冲突，正交性良好。然而，父节点公式中的 C_total 定义为 'N4 计算的 TCO'，但提供的两个子节点均未涉及 C_total 的定义或计算方式，导致关键变量缺失，不完备。）

## Search Query

cost per quality adjusted token definition LLM inference benchmark
