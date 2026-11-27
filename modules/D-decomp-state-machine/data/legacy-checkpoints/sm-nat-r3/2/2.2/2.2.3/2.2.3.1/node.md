# N150: 描述大小 S 与热度 R 负相关 (ρ=-0.3) 的 Gaussian Copula 密度函数 f_{S,R}(s, r) = φ(Φ_S^{-1}(s), 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

描述大小 S 与热度 R 负相关 (ρ=-0.3) 的 Gaussian Copula 密度函数 f_{S,R}(s, r) = φ(Φ_S^{-1}(s), Φ_R^{-1}(r), ρ) * f_S(s) * f_R(r)，用于生成符合相关性的联合样本。

## Corrected Claim

描述大小 S 与热度 R 负相关 (ρ=-0.3) 的 Gaussian Copula 密度函数 f_{S,R}(s, r) = φ(Φ_S^{-1}(s), Φ_R^{-1}(r), ρ) * f_S(s) * f_R(r)，用于生成符合相关性的联合样本。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式是 Gaussian Copula 构造联合分布的标准定义，数学推导自洽。
