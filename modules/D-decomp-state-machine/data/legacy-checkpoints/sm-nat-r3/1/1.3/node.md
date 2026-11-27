# N8: 联合分布形态：大小 S 与热度 R 的负相关 (ρ≈-0.3) 意味着热门对象倾向于较小，需定义联合 CDF F(S,R) 或通过 Copula 函数（如 Cl

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

联合分布形态：大小 S 与热度 R 的负相关 (ρ≈-0.3) 意味着热门对象倾向于较小，需定义联合 CDF F(S,R) 或通过 Copula 函数（如 Clayton Copula）量化依赖结构。

## Corrected Claim

联合分布形态：大小 S 与热度 R 的负相关 (ρ≈-0.3) 意味着热门对象倾向于较小，需定义联合 CDF F(S,R) 或通过 Copula 函数（如 Clayton Copula）量化依赖结构。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在严重逻辑矛盾与冗余。节点1声称使用Clayton建模负相关，节点2指出Clayton无法建模负相关（事实正确，Clayton通常用于正相关，尽管其Spearman相关系数公式在θ>0时为正），节点3又转向Gumbel。然而，Gumbel Copula通常也用于建模正相关（上尾依赖），且其Spearman相关系数公式 ρ_S = θ/(2θ+1) 在 θ>0 时为正，无法直接通过简单的 θ>0 反解出负相关（需 θ<0，但Gumbel定义域通常 θ≥1 或 θ>0）。Frank Copula 才是能同时建模正负相关的常见选择。此外，节点1和节点2在方法论上直接冲突，节点3的数学推导前提（Gumbel用于负相关且公式适用）存在严重学术错误。）
