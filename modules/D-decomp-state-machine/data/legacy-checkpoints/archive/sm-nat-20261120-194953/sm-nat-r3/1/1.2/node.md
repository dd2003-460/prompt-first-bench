# N7: 请求热度分布 $R$ 为帕累托分布：$P(R=r) = \beta R_{min}^\beta / r^{\beta+1}$，其中 $\beta=0.9$，$R

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

请求热度分布 $R$ 为帕累托分布：$P(R=r) = \beta R_{min}^\beta / r^{\beta+1}$，其中 $\beta=0.9$，$R_{min}=1$ req/day，需确认 $\beta < 1$ 导致总请求量发散，因此必须引入截断或归一化常数 $C = \sum_{i=1}^{10^5} R_i$ 以匹配 5000 万次/天的约束。

## Corrected Claim

请求热度分布 $R$ 为帕累托分布：$P(R=r) = \beta R_{min}^\beta / r^{\beta+1}$，其中 $\beta=0.9$，$R_{min}=1$ req/day，需确认 $\beta < 1$ 导致总请求量发散，因此必须引入截断或归一化常数 $C = \sum_{i=1}^{10^5} R_i$ 以匹配 5000 万次/天的约束。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 769)
