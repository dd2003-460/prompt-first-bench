# N95: t检验统计量计算：t = k / SE_k，其中 SE_k 为 k 的标准误。根据 CLT，SE_k = σ_k / sqrt(n)。若 n=100, σ_k=

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

t检验统计量计算：t = k / SE_k，其中 SE_k 为 k 的标准误。根据 CLT，SE_k = σ_k / sqrt(n)。若 n=100, σ_k=20%（周期波动率），则 SE_k=2%，对应 k=10% 时 t=5；若 n=100, σ_k=10%，则 SE_k=1%，对应 k=2% 时 t=2。

## Corrected Claim

t检验统计量计算：t = k / SE_k，其中 SE_k 为 k 的标准误。根据 CLT，SE_k = σ_k / sqrt(n)。若 n=100, σ_k=20%（周期波动率），则 SE_k=2%，对应 k=10% 时 t=5；若 n=100, σ_k=10%，则 SE_k=1%，对应 k=2% 时 t=2。

## Evidence

父节点级核验未通过：不完备（子节点分别处理了参数估计（σ_k）、样本量修正（n_eff）和替代检验方法，三者关注点不同，无重叠或矛盾，正交性良好。但父节点核心是 t 统计量的计算逻辑及基于 CLT 的推导，子节点遗漏了“t 统计量计算公式本身”或“自由度/临界值判断”等核心计算步骤的明确分解，且未直接覆盖父节点中具体的数值推导逻辑（如 n=100 时的具体计算过程），导致完备性不足。）
