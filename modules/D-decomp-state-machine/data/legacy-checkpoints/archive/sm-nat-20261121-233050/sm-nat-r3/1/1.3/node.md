# N8: 大小与热度的联合分布相关性量化：基于 ρ ≈ -0.3，构建 Copula 函数（如 Gaussian Copula 或 Gumbel-Hougaard）来描述

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

大小与热度的联合分布相关性量化：基于 ρ ≈ -0.3，构建 Copula 函数（如 Gaussian Copula 或 Gumbel-Hougaard）来描述 S_i 和 F_i 的联合概率密度 P(S,F)，用于计算加权命中率。

## Corrected Claim

大小与热度的联合分布相关性量化：基于 ρ ≈ -0.3，构建 Copula 函数（如 Gaussian Copula 或 Gumbel-Hougaard）来描述 S_i 和 F_i 的联合概率密度 P(S,F)，用于计算加权命中率。

## Evidence

父节点级核验未通过：不完备（子节点1（构造）与子节点3（敏感性）在数学定义上存在轻微重叠（都涉及Copula参数设置），但逻辑上分别对应'建模'与'验证'，可视为正交。主要问题在于完备性：父节点明确提到'Gaussian Copula 或 Gumbel-Hougaard'，但子节点仅涵盖了Gaussian Copula的构造和基于ρ的分析，完全缺失了Gumbel-Hougaard Copula（通常用于处理尾部相关性，且其参数含义与Pearson ρ不同）的构造、适用场景对比及联合密度计算。此外，父节点目标是'计算加权命中率'，子节点2仅计算了字节覆盖差异ΔBytes，未直接关联到最终的'加权命中率'公式或指标定义。）

## Search Query

Pareto distribution correlation copula cache simulation
