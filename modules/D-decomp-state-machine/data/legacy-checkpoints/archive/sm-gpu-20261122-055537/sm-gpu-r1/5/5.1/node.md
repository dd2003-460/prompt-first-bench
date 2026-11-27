# N24: 性价比指标定义：Cost_Efficiency = C_total / (Q_score * T_throughput)，其中 C_total 为 N4 计算的

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

性价比指标定义：Cost_Efficiency = C_total / (Q_score * T_throughput)，其中 C_total 为 N4 计算的 TCO，Q_score 为精度损失调整后的质量得分(0-1)，T_throughput 为 tokens/s。该指标将延迟(性能变量)转化为吞吐量，与成本和质量挂钩。

## Corrected Claim

性价比指标定义：Cost_Efficiency = C_total / (Q_score * T_throughput)，其中 C_total 为 N4 计算的 TCO，Q_score 为精度损失调整后的质量得分(0-1)，T_throughput 为 tokens/s。该指标将延迟(性能变量)转化为吞吐量，与成本和质量挂钩。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cost per quality adjusted token definition LLM inference benchmark
