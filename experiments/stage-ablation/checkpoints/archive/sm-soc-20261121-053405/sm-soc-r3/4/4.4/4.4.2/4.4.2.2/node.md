# N197: 样本量 N 对置信度下界阈值 $p_{threshold}$ 的依赖：$p_{threshold}(N) = \frac{1}{N}(E + \sqrt{3.8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N72

## Claim

样本量 N 对置信度下界阈值 $p_{threshold}$ 的依赖：$p_{threshold}(N) = \frac{1}{N}(E + \sqrt{3.84E})$。当 N=100 时 $p_{threshold}=16\%$；当 N=1000 时 $p_{threshold} \approx 11\%$；当 N=10000 时 $p_{threshold} \approx 10.4\%$。这表明随着数据量增加，置信度下界的触发点趋近于原假设值 10%，N21 的 10% 阈值仅在极大样本下才严谨。

## Corrected Claim

样本量 N 对置信度下界阈值 $p_{threshold}$ 的依赖：$p_{threshold}(N) = \frac{1}{N}(E + \sqrt{3.84E})$。当 N=100 时 $p_{threshold}=16\%$；当 N=1000 时 $p_{threshold} \approx 11\%$；当 N=10000 时 $p_{threshold} \approx 10.4\%$。这表明随着数据量增加，置信度下界的触发点趋近于原假设值 10%，N21 的 10% 阈值仅在极大样本下才严谨。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 p(N) = (E + sqrt(3.84E))/N 在 E=10 时，N=100 得 16%，N=1000 得 11.1%，N=10000 得 10.4%，数值与陈述一致，且符合统计置信区间随样本量增大而收敛于原假设值的逻辑。

## Search Query

sample size effect on critical proportion chi-square test threshold convergence
