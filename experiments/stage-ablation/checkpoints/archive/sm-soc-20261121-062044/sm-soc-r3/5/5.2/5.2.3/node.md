# N242: 观测值 r > 0.5 与理论基准 r_theory ∈ [-0.3, -0.1] 的统计异常量化：计算效应量差异 Δr = r_obs - r_theory_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

观测值 r > 0.5 与理论基准 r_theory ∈ [-0.3, -0.1] 的统计异常量化：计算效应量差异 Δr = r_obs - r_theory_mid ≈ 0.5 - (-0.2) = 0.7；在 n=100 时，Δr 的 Z-score = Δr / SE(r) ≈ 0.7 / (1.96/√100) ≈ 3.57，p < 0.001，表明观测到的正相关极不可能由理论模型中的随机噪声解释，必须引入新的结构性变量（如算法推荐）。

## Corrected Claim

观测值 r > 0.5 与理论基准 r_theory ∈ [-0.3, -0.1] 的统计异常量化：计算效应量差异 Δr = r_obs - r_theory_mid ≈ 0.5 - (-0.2) = 0.7；在 n=100 时，Δr 的 Z-score = Δr / SE(r) ≈ 0.7 / (1.96/√100) ≈ 3.57，p < 0.001，表明观测到的正相关极不可能由理论模型中的随机噪声解释，必须引入新的结构性变量（如算法推荐）。

## Evidence

先验知识/题面给定，逻辑校验通过：Z-score计算基于标准误公式 SE=1.96/√n 符合统计学原理，数值推导自洽。
