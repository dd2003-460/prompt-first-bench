# N97: 若改用 Frank Copula 建模 ρ=-0.3，其参数 θ 需通过求解 Corr(S,H) = -0.3 的数值方程确定，Frank Copula 的相关

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

若改用 Frank Copula 建模 ρ=-0.3，其参数 θ 需通过求解 Corr(S,H) = -0.3 的数值方程确定，Frank Copula 的相关系数公式为 ρ = (e^θ - 1 - θ e^θ) / (θ^2 e^θ)，解得 θ ≈ -1.58（需数值验证）

## Corrected Claim

若改用 Frank Copula 建模 ρ=-0.3，其参数 θ 需通过求解 Corr(S,H) = -0.3 的数值方程确定，Frank Copula 的相关系数公式为 ρ = (e^θ - 1 - θ e^θ) / (θ^2 e^θ)，解得 θ ≈ -1.58（需数值验证）

## Evidence

父节点级核验未通过：不完备（子节点之间存在正交性（一个关注数值验证，一个关注理论性质），但存在严重的事实错误导致完备性和正确性受损。Frank Copula 的参数 θ 通常定义在 (0, ∞) 范围内以表示正相关，其 Spearman 相关系数 ρ 随 θ 增加而增加。对于负相关，Frank Copula 并不直接支持 θ < 0 的标准定义（通常使用反演或不同的 Copula 如 Clayton 的逆，或者更常见的，Frank Copula 仅用于正相关，负相关需使用其他 Copula 或调整定义）。此外，公式 ρ = (e^θ - 1 - θ e^θ) / (θ^2 e^θ) 在 θ < 0 时的行为描述有误，且 θ ≈ -1.58 这一解在标准 Frank Copula 定义下是不成立的（标准定义下 θ>0 对应 ρ>0）。因此，子节点基于错误的数学前提，未能正确覆盖父节点中隐含的‘如何求解’及‘为何适用’的逻辑，反而引入了误导性内容。）

## Search Query

Frank copula parameter theta for correlation -0.3 numerical solution
