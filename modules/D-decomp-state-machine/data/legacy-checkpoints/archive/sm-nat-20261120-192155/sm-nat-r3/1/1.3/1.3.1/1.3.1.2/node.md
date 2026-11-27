# N74: 负相关项 exp(-0.3 * (ln(i) - E[ln(i)])) 的解析简化：在 Pareto 分布下，ln(i) 的期望 E[ln(i)] 对于 i=1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

负相关项 exp(-0.3 * (ln(i) - E[ln(i)])) 的解析简化：在 Pareto 分布下，ln(i) 的期望 E[ln(i)] 对于 i=1..N 近似为 ln(N)/2；因此修正项为 exp(-0.3 * (ln(i) - 0.5*ln(100000))) = exp(-0.3 * ln(i) + 0.3 * 5.756) = i^{-0.3} * e^{1.727} ≈ 5.62 * i^{-0.3}。

## Corrected Claim

负相关项 exp(-0.3 * (ln(i) - E[ln(i)])) 的解析简化：在 Pareto 分布下，ln(i) 的期望 E[ln(i)] 对于 i=1..N 近似为 ln(N)/2；因此修正项为 exp(-0.3 * (ln(i) - 0.5*ln(100000))) = exp(-0.3 * ln(i) + 0.3 * 5.756) = i^{-0.3} * e^{1.727} ≈ 5.62 * i^{-0.3}。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布下ln(i)的期望近似为ln(N)/2符合数学直觉，数值计算exp(1.727)≈5.62准确，推导过程自洽。
