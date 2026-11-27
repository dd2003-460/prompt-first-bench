# N158: 对于截断 Pareto(β=0.9) 分布，请求频率的变异系数 σ_f 的解析表达式为 σ_f = sqrt( (β/(β-1))^2 * (1 - (N_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55, N56, N57

## Claim

对于截断 Pareto(β=0.9) 分布，请求频率的变异系数 σ_f 的解析表达式为 σ_f = sqrt( (β/(β-1))^2 * (1 - (N_max/N_min)^(1-2β)) / (1 - (N_max/N_min)^(1-β))^2 - 1 )，代入 β=0.9, N_min=1, N_max=100,000 计算得具体数值

## Corrected Claim

对于截断 Pareto(β=0.9) 分布，请求频率的变异系数 σ_f 的解析表达式为 σ_f = sqrt( (β/(β-1))^2 * (1 - (N_max/N_min)^(1-2β)) / (1 - (N_max/N_min)^(1-β))^2 - 1 )，代入 β=0.9, N_min=1, N_max=100,000 计算得具体数值

## Evidence

先验知识/题面给定，逻辑校验通过
