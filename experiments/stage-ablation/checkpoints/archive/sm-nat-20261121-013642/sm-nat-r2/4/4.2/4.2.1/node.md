# N60: R_bytes (总字节请求率) 的计算表达式：R_bytes = (50,000,000 requests/day) * E[Size | Pareto(α=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

R_bytes (总字节请求率) 的计算表达式：R_bytes = (50,000,000 requests/day) * E[Size | Pareto(α=1.1)]，其中 E[Size] = s_min * α / (α-1) (需设定 s_min 并截断以匹配 128GB 总容量约束或取前 100k 对象均值)，单位为 GB/day。

## Corrected Claim

R_bytes (总字节请求率) 的计算表达式：R_bytes = (50,000,000 requests/day) * E[Size | Pareto(α=1.1)]，其中 E[Size] = s_min * α / (α-1) (需设定 s_min 并截断以匹配 128GB 总容量约束或取前 100k 对象均值)，单位为 GB/day。

## Evidence

[质询]Pareto分布的期望值公式 E[Size] = s_min * α / (α-1) 仅在 α > 1 时收敛，且该公式计算的是理论均值。若未明确截断（truncation）或有限样本（如前100k对象），直接使用该均值可能导致总容量远超128GB约束，或者在α接近1时数值爆炸。但陈述中已注明“需设定 s_min 并截断以匹配 128GB 总容量约束或取前 100k 对象均值”，这涵盖了工程实现中的必要修正，因此逻辑上是自洽的。 | 先验知识/题面给定，逻辑校验通过。Pareto分布期望公式正确（α>1），且陈述中包含了针对有限容量约束的工程化处理说明，符合系统建模逻辑。
