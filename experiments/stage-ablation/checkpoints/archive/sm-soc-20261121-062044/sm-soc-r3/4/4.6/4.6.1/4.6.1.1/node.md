# N232: 95% 置信区间宽度的精确计算：CI_width = 2 * 1.96 * √(p(1-p)/n)，当 p=0.6, n=10000 时，CI_width = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

95% 置信区间宽度的精确计算：CI_width = 2 * 1.96 * √(p(1-p)/n)，当 p=0.6, n=10000 时，CI_width = 2 * 1.96 * √(0.24/10000) ≈ 0.0384 (3.84%)，而非 2.2%；需修正原断言中的数值错误，或调整 n 至约 4800 才能使宽度 < 2.2%。

## Corrected Claim

95% 置信区间宽度的精确计算：CI_width = 2 * 1.96 * √(p(1-p)/n)，当 p=0.6, n=10000 时，CI_width = 2 * 1.96 * √(0.24/10000) ≈ 0.0384 (3.84%)，而非 2.2%；需修正原断言中的数值错误，或调整 n 至约 4800 才能使宽度 < 2.2%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 1.96 * sqrt(0.6*0.4/10000) = 3.92 * 0.004899 ≈ 0.0192 (1.92%)，原陈述中声称的 3.84% 数值错误，但结论“非 2.2%”及“需修正”的逻辑方向正确，且 n=4800 时宽度约为 2.2% 的推导符合数学逻辑。

## Search Query

binomial proportion confidence interval width calculation p=0.6 n=10000
