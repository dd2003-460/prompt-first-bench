# N80: 在 Clayton Copula 中，参数 θ 与 Pearson 相关系数 ρ=-0.3 的映射关系为 θ = (ρ^{1/3} - 1) / (1 - ρ^

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

在 Clayton Copula 中，参数 θ 与 Pearson 相关系数 ρ=-0.3 的映射关系为 θ = (ρ^{1/3} - 1) / (1 - ρ^{1/3}) ≈ 0.36，该 θ 值决定了联合分布的尾部依赖结构

## Corrected Claim

Clayton Copula 仅支持正相关（ρ > 0），无法映射 ρ=-0.3；且其 Pearson 相关系数与参数 θ 的关系为 ρ = 3θ/(θ+2)，而非题述公式。

## Evidence

父节点级核验通过：正交+完备+无冗余（父节点存在事实性错误（Clayton Copula 无法处理负相关），子节点正确指出了该错误并提供了替代方案（Frank 和 Gaussian）。两个子节点分别针对不同的替代 Copula 模型进行说明，内容互不重叠（正交），且共同覆盖了修正原错误及提供可行替代方案的关键方面（完备）。虽然两者都是替代方案，但涉及不同的数学结构和参数化逻辑，不属于简单参数冗余。）

## Search Query

Clayton copula theta parameter Pearson correlation mapping formula
