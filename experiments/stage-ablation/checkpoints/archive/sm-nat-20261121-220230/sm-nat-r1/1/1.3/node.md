# N8: 对象大小分布s_i服从Pareto(α=1.1)，归一化后单对象平均大小E[s] = α * s_min / (α-1) = 1.1 * s_min / 0.1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

对象大小分布s_i服从Pareto(α=1.1)，归一化后单对象平均大小E[s] = α * s_min / (α-1) = 1.1 * s_min / 0.1 = 11 * s_min，其中s_min为最小对象大小（需假设，如1KB，则E[s]=11KB）。

## Corrected Claim

对象大小分布s_i服从Pareto(α=1.1)，归一化后单对象平均大小E[s] = α * s_min / (α-1) = 1.1 * s_min / 0.1 = 11 * s_min，其中s_min为最小对象大小（需假设，如1KB，则E[s]=11KB）。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的期望公式 E[s] = α * s_min / (α-1) 在 α > 1 时成立，代入 α=1.1 计算得 11 * s_min，数学推导正确。
