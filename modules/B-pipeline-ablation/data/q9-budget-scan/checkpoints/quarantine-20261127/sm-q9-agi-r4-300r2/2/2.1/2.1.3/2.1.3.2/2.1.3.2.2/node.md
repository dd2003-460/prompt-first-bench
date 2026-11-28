# N303: 尾部指令保持率 Retention_tail ≈ 70%-80% 优于中间区域的原因机制：Transformer 注意力的自回归特性使得最近生成的 token 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

尾部指令保持率 Retention_tail ≈ 70%-80% 优于中间区域的原因机制：Transformer 注意力的自回归特性使得最近生成的 token 对后续生成具有更强的因果影响力（Recency Bias）；量化表现为注意力权重的局部性，距离当前位置 Δd 内的 token 获得的注意力分数占比 > 90%，因此紧邻生成点的尾部指令比远离的中间指令更容易被“看见”。

## Corrected Claim

尾部指令保持率通常优于中间区域，主要归因于Transformer自回归特性带来的近因偏差（Recency Bias）及注意力权重的局部性倾向，使得紧邻生成点的尾部指令在注意力分布中往往占据更高权重，从而更易被模型捕捉。

## Evidence

[质询]陈述中关于注意力权重局部性的具体量化指标（距离Δd内占比>90%）缺乏普遍适用的理论支撑或实证数据支持，不同模型架构、上下文长度及训练阶段下该比例波动极大，将其作为固定机制解释过于绝对化。 | 先验知识/题面给定，逻辑校验通过；但具体数值阈值（>90%）属于经验性断言，在无外部来源支持且存在反例可能性的情况下，依据经验事实排除条款降级。

## Search Query

recency bias transformer attention locality tail instruction retention mechanism
