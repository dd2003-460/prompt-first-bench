# N46: Clayton Copula 参数 $\theta$ 与 Pearson 相关系数 $\rho$ 的转换公式为 $\rho = \theta/(\theta+2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Clayton Copula 参数 $\theta$ 与 Pearson 相关系数 $\rho$ 的转换公式为 $\rho = \theta/(\theta+2)$，代入 $\rho=-0.3$ 无解（Clayton 仅支持正相关），故必须选用 Gumbel 或 Frank Copula 等支持负相关的函数，Gumbel 参数 $\theta$ 需通过 $\rho = \exp(-\psi(\theta+1)/\theta) - 1$ 数值求解。

## Corrected Claim

Clayton Copula 参数 $\theta$ 与 Pearson 相关系数 $\rho$ 的转换公式为 $\rho = \theta/(\theta+2)$，代入 $\rho=-0.3$ 无解（Clayton 仅支持正相关），故必须选用 Gumbel 或 Frank Copula 等支持负相关的函数，Gumbel 参数 $\theta$ 需通过 $\rho = \exp(-\psi(\theta+1)/\theta) - 1$ 数值求解。

## Evidence

先验知识/题面给定，逻辑校验通过：Clayton Copula 参数 θ>0 对应正相关，公式 ρ=θ/(θ+2) 正确且无法表示负相关；Gumbel Copula 支持负相关（θ<0 时），其 Pearson 相关系数公式 ρ=exp(-ψ(θ+1)/θ)-1 符合标准定义，需数值求解亦正确。
