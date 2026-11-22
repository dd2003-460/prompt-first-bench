# N8: 大小 S 与热度 R 的负相关系数 ρ≈-0.3 需通过 Copula 函数（如 Gaussian Copula 或 Clayton Copula）构建联合分布

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

大小 S 与热度 R 的负相关系数 ρ≈-0.3 需通过 Copula 函数（如 Gaussian Copula 或 Clayton Copula）构建联合分布 F(S,R)，以捕捉边缘分布与依赖结构的完整联合概率密度函数 f(S,R)

## Corrected Claim

大小 S 与热度 R 的负相关系数 ρ≈-0.3 需通过 Copula 函数（如 Gaussian Copula 或 Clayton Copula）构建联合分布 F(S,R)，以捕捉边缘分布与依赖结构的完整联合概率密度函数 f(S,R)

## Evidence

父节点级核验未通过：不完备（子节点分别描述了Gaussian和Clayton两种Copula，内容不重叠且无矛盾，正交性满足；但父节点要求'构建联合分布以捕捉...完整联合概率密度函数'，而子节点仅给出公式推导，未涵盖实际建模步骤（如边缘分布拟合、参数估计、密度计算等），完备性不足。）
