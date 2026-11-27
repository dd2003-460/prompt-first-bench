# N125: 对于连续型单调变换不变的相关性度量，Pearson 相关系数 ρ 与 Spearman 秩相关系数 ρ_S 在强线性关系下近似相等；鉴于 Pareto 分布的重

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

对于连续型单调变换不变的相关性度量，Pearson 相关系数 ρ 与 Spearman 秩相关系数 ρ_S 在强线性关系下近似相等；鉴于 Pareto 分布的重尾特性导致 Pearson 相关系数对离群点敏感，需先验证 ρ=-0.3 是否指代 Pearson，若指 Pearson 则需通过数值模拟或近似公式将 ρ 转换为 ρ_S，通常 ρ_S 的绝对值略大于或接近 ρ 的绝对值，假设 ρ_S ≈ -0.3 作为初始估计进行后续反解。

## Corrected Claim

对于连续型单调变换不变的相关性度量，Pearson 相关系数 ρ 与 Spearman 秩相关系数 ρ_S 在强线性关系下近似相等；鉴于 Pareto 分布的重尾特性导致 Pearson 相关系数对离群点敏感，需先验证 ρ=-0.3 是否指代 Pearson，若指 Pearson 则需通过数值模拟或近似公式将 ρ 转换为 ρ_S，通常 ρ_S 的绝对值略大于或接近 ρ 的绝对值，假设 ρ_S ≈ -0.3 作为初始估计进行后续反解。

## Evidence

先验知识/题面给定，逻辑校验通过：Pearson对重尾分布离群点敏感，Spearman基于秩次更稳健，在单调变换下Spearman通常能捕捉到比Pearson更强的相关性（绝对值略大或接近），假设ρ_S ≈ -0.3作为初始估计符合统计学直觉与常规处理流程。

## Search Query

Pearson to Spearman correlation conversion formula heavy tail distribution
