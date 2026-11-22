# N28: 截断帕累托分布 $S$ 的期望值 $E[S]$ 计算结果为 11.11 KB，基于公式 $E[S] = \frac{\alpha S_{min}}{\alpha

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

截断帕累托分布 $S$ 的期望值 $E[S]$ 计算结果为 11.11 KB，基于公式 $E[S] = \frac{\alpha S_{min}}{\alpha-1}(1 - (S_{min}/S_{max})^{\alpha-1})$ 代入 $\alpha=1.1, S_{min}=1\text{KB}, S_{max}=100\text{MB}$ 得出，该值收敛且远小于缓存容量限制。

## Corrected Claim

截断帕累托分布 $S$ 的期望值 $E[S]$ 计算结果为 11.11 KB，基于公式 $E[S] = \frac{\alpha S_{min}}{\alpha-1}(1 - (S_{min}/S_{max})^{\alpha-1})$ 代入 $\alpha=1.1, S_{min}=1\text{KB}, S_{max}=100\text{MB}$ 得出，该值收敛且远小于缓存容量限制。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 8 column 44 (char 343)
