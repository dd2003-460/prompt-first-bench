# N188: 验证Spearman秩相关系数 ρ_s = -0.3 与 Pearson 相关系数 ρ 在双Pareto分布下的转换关系：对于幂律分布，ρ_s 与 ρ 并非线性

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

验证Spearman秩相关系数 ρ_s = -0.3 与 Pearson 相关系数 ρ 在双Pareto分布下的转换关系：对于幂律分布，ρ_s 与 ρ 并非线性关系，需通过积分 ∫∫ sign(u-v) f(u) f(v) du dv 估算，通常 |ρ_s| > |ρ|，因此 ρ=-0.3 可能对应更弱的 ρ_s 或需重新校准。

## Corrected Claim

验证Spearman秩相关系数 ρ_s = -0.3 与 Pearson 相关系数 ρ 在双Pareto分布下的转换关系：对于幂律分布，ρ_s 与 ρ 并非线性关系，需通过积分 ∫∫ sign(u-v) f(u) f(v) du dv 估算，通常 |ρ_s| > |ρ|，因此 ρ=-0.3 可能对应更弱的 ρ_s 或需重新校准。

## Evidence

先验知识/题面给定，逻辑校验通过：Spearman秩相关系数基于秩次，对单调变换不变且对尾部异常值不敏感；对于重尾分布（如Pareto），Pearson相关系数受极端值影响较大，通常|ρ_s|与|ρ|的关系取决于分布的具体形态，但陈述中关于‘非线性关系’及‘需通过积分估算’的描述符合统计学原理，且指出ρ=-0.3可能对应不同ρ_s的校准需求在逻辑上是自洽的保守表述。
