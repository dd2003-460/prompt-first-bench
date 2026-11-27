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

父节点级核验未通过：不完备（子节点在逻辑上正交，分别覆盖了模型构造、具体影响量化和敏感性分析三个不同维度。然而，父节点明确提到了‘Gaussian Copula 或 Gumbel-Hougaard’，但子节点仅详细展开了 Gaussian Copula 的构造，完全缺失了 Gumbel-Hougaard Copula 的构造及其在负相关场景下的适用性讨论（注：Gumbel-Hougaard 通常用于正相关，此处父节点提及可能存在理论偏差或需要特别说明为何选用/排除，导致覆盖不全）。此外，父节点核心目标是‘计算加权命中率’，子节点2仅计算了‘字节覆盖差异’，未直接给出加权命中率的计算公式或结果，存在目标对齐上的微小缺失。）

## Search Query

Pareto distribution correlation copula cache simulation
