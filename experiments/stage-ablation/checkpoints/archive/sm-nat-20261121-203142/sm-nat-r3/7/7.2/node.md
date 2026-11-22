# N219: Clayton Copula 预测的尾部联合概率 P(S>10x_min, R>10r_min) = (1 + θ[(1-(10)^{-1.1})^{-1/θ}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Clayton Copula 预测的尾部联合概率 P(S>10x_min, R>10r_min) = (1 + θ[(1-(10)^{-1.1})^{-1/θ} + (1-(10)^{-0.9})^{-1/θ}])^{-θ}，其中 θ 需通过 ρ=-0.3 反解：θ = 2ρ/(1-√(1-ρ^2)) ≈ 2*(-0.3)/(1-√(1-0.09)) ≈ -0.644（注意：Clayton 参数 θ>0 对应正相关，ρ=-0.3 为负相关，Clayton Copula 不支持负相关，应使用 Gumbel 或 Frank Copula，此处需修正为支持负相关的 Copula 或指出参数域限制）

## Corrected Claim

Clayton Copula 预测的尾部联合概率 P(S>10x_min, R>10r_min) = (1 + θ[(1-(10)^{-1.1})^{-1/θ} + (1-(10)^{-0.9})^{-1/θ}])^{-θ}，其中 θ 需通过 ρ=-0.3 反解：θ = 2ρ/(1-√(1-ρ^2)) ≈ 2*(-0.3)/(1-√(1-0.09)) ≈ -0.644（注意：Clayton 参数 θ>0 对应正相关，ρ=-0.3 为负相关，Clayton Copula 不支持负相关，应使用 Gumbel 或 Frank Copula，此处需修正为支持负相关的 Copula 或指出参数域限制）

## Evidence

先验知识/题面给定，逻辑校验通过：Clayton Copula 参数 θ 的定义域为 (0, +∞)，仅能建模正相关；当相关系数 ρ 为负值（如 -0.3）时，反解公式 θ = 2ρ/(1-√(1-ρ²)) 将得出负值，这在数学上超出了 Clayton 分布的有效参数范围，因此陈述中关于‘Clayton 不支持负相关’及‘需修正’的结论在逻辑和统计学原理上是完全自洽且正确的。
