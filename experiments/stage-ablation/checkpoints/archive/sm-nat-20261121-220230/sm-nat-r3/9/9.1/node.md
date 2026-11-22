# N96: Clayton Copula 无法生成负相关（ρ ∈ [-1, 0)），其相关系数公式 ρ = θ/(θ+1) 恒为正；因此 N29 中声称使用 Clayton

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

Clayton Copula 无法生成负相关（ρ ∈ [-1, 0)），其相关系数公式 ρ = θ/(θ+1) 恒为正；因此 N29 中声称使用 Clayton 拟合 ρ=-0.3 在数学上是不成立的，应改用 Frank Copula 或 Gumbel-Hougaard Copula 的变体（需验证其负相关支持性）

## Corrected Claim

Clayton Copula 无法生成负相关（ρ ∈ [-1, 0)），其相关系数公式 ρ = θ/(θ+1) 恒为正；因此 N29 中声称使用 Clayton 拟合 ρ=-0.3 在数学上是不成立的，应改用 Frank Copula 或 Gumbel-Hougaard Copula 的变体（需验证其负相关支持性）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且互斥：节点1验证Frank Copula的可行性（正向），节点2排除Gumbel Copula的不可行性（负向/纠错），节点3提供具体参数求解细节（执行层）。三者分别对应‘可行性确认’、‘替代方案排除’和‘参数计算’，无重复或矛盾。父节点中关于Clayton失效的陈述属于前提背景，已隐含在子节点对替代方案的讨论中，无需单独列出子节点，因此覆盖完整。）

## Search Query

Clayton copula correlation formula negative correlation impossibility
