# N71: Clayton Copula 参数 θ 与 Pearson 相关系数 ρ=-0.3 之间的映射关系，用于确定联合分布的具体形态，θ = ((ρ^(-2/3)) 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

Clayton Copula 参数 θ 与 Pearson 相关系数 ρ=-0.3 之间的映射关系，用于确定联合分布的具体形态，θ = ((ρ^(-2/3)) - 1) * 3。

## Corrected Claim

Clayton Copula 参数 θ 与 Pearson 相关系数 ρ=-0.3 之间的映射关系，用于确定联合分布的具体形态，θ = ((ρ^(-2/3)) - 1) * 3。

## Evidence

父节点级核验未通过：非正交, 不完备（1. 数学错误导致非正交/矛盾：Clayton Copula 的线性参数 θ 与 Pearson 相关系数 ρ 之间不存在简单的闭式映射公式 θ = ((ρ^(-2/3)) - 1) * 3（该公式形式更接近 Gumbel 或误用）。通常需要通过数值方法求解。子节点 1 基于错误的公式得出 θ≈0.9，而子节点 2 给出的 CDF 表达式中，当 θ<1 时，指数项 -θ/(θ-1) 为正，且结构疑似混淆了 Clayton 与 Gumbel 或 Frank 的形式，导致两个子节点在数学逻辑上不自洽且相互矛盾。2. 完备性不足：父节点强调“映射关系”，子节点未指出该映射需数值求解或公式本身存疑，仅给出了一个错误的直接计算，未能覆盖“如何正确确定参数”这一关键方面。）

## Search Query

Clayton copula parameter theta from correlation coefficient
