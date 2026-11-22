# N6: 对象大小分布 $S$ 为截断帕累托分布：$P(S=s) = \alpha S_{min}^\alpha / s^{\alpha+1}$，其中 $\alpha=1

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

对象大小分布 $S$ 为截断帕累托分布：$P(S=s) = \alpha S_{min}^\alpha / s^{\alpha+1}$，其中 $\alpha=1.1$，$S_{min}=1$ KB（假设），$S_{max}=100$ MB（假设），需验证 $E[S] = \frac{\alpha S_{min}}{\alpha-1}(1 - (S_{min}/S_{max})^{\alpha-1})$ 是否收敛且均值合理。

## Corrected Claim

对象大小分布 $S$ 为截断帕累托分布：$P(S=s) = \alpha S_{min}^\alpha / s^{\alpha+1}$，其中 $\alpha=1.1$，$S_{min}=1$ KB（假设），$S_{max}=100$ MB（假设），需验证 $E[S] = \frac{\alpha S_{min}}{\alpha-1}(1 - (S_{min}/S_{max})^{\alpha-1})$ 是否收敛且均值合理。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 778)

## Search Query

truncated Pareto distribution mean expectation formula alpha 1.1
