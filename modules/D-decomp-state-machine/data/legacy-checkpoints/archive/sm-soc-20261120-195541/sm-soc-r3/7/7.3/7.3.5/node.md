# N189: 均衡点动态稳定性判据：Jacobian 矩阵 J = ∂(ΔP_ask, ΔT_deal)/∂(P_ask, T_deal) 的特征值 λ1, λ2 需满足 |

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

均衡点动态稳定性判据：Jacobian 矩阵 J = ∂(ΔP_ask, ΔT_deal)/∂(P_ask, T_deal) 的特征值 λ1, λ2 需满足 |λ1| < 1 且 |λ2| < 1，否则均衡发散；需计算在 β_platform 动态调整下 J 的特征值变化，验证系统是否收敛。

## Corrected Claim

均衡点动态稳定性判据：Jacobian 矩阵 J = ∂(ΔP_ask, ΔT_deal)/∂(P_ask, T_deal) 的特征值 λ1, λ2 需满足 |λ1| < 1 且 |λ2| < 1，否则均衡发散；需计算在 β_platform 动态调整下 J 的特征值变化，验证系统是否收敛。

## Evidence

先验知识/题面给定，逻辑校验通过：离散动态系统的局部稳定性判据确实要求雅可比矩阵特征值的模小于1，该陈述符合控制论与动力系统的基本原理。
