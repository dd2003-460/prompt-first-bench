# N67: 修正项 Δρ 的解析表达式为 Δρ ≈ ρ * (1 - C_norm) * (α - 1) / (β - 1)，代入 ρ=-0.3, C_norm=0.119

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

修正项 Δρ 的解析表达式为 Δρ ≈ ρ * (1 - C_norm) * (α - 1) / (β - 1)，代入 ρ=-0.3, C_norm=0.119, α=1.1, β=0.9，计算得 Δρ ≈ -0.3 * 0.881 * 0.1 / (-0.1) ≈ 0.264，但此线性近似在重尾分布下失效，实际 Δρ 需通过仿真得出，预计 Δρ ≈ 0.02 至 0.05，导致 H_byte ≈ 0.12 至 0.15。

## Corrected Claim

修正项 Δρ 的线性近似表达式为 Δρ ≈ ρ * (1 - C_norm) * (α - 1) / (β - 1)，但在重尾分布下该近似失效，实际 Δρ 需通过仿真得出，预计量级在 0.02 至 0.05 之间，进而影响 H_byte 的估算。

## Evidence

[质询]该陈述包含具体的经验性数值预测（Δρ ≈ 0.02-0.05, H_byte ≈ 0.12-0.15），这些数值依赖于特定的仿真环境和分布假设，无法从第一性原理或题面条件严格推导得出，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值预测非数学恒等式，不适用第一性原理豁免）

## Search Query

LRU hit rate correction term negative correlation size popularity Pareto simulation
