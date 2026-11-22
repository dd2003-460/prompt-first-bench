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

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在严重逻辑矛盾和事实错误。1. 子节点1声称用Clayton建模负相关，但子节点2指出Clayton仅支持正相关（实际上Clayton通常用于正相关，且其相关系数公式 ρ=θ/(2θ+1) 在 θ>0 时为正，无法反解出负相关），两者直接矛盾。2. 子节点3声称Gumbel Copula建模负相关，但Gumbel Copula实际上也仅支持正相关（其Spearman相关系数 ρ_S = (θ-1)/(θ+1) 在 θ>1 时为正），且给出的公式 ρ_S = θ/(2θ+1) 是Clayton的公式，张冠李戴，事实错误。3. 负相关应使用如Frank Copula（支持负相关）或Gaussian Copula（支持任意相关）建模，而非Gumbel或Clayton。4. 子节点1和3重复了“需反解参数”的步骤，存在冗余。）
