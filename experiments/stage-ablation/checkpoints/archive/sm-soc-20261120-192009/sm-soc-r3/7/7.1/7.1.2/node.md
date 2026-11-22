# N304: CTR 置信区间构造：采用 Wilson 区间或 Clopper-Pearson 区间而非简单正态近似，公式为 [p̂/(1+z²/n) ± z*sqrt(p̂

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

CTR 置信区间构造：采用 Wilson 区间或 Clopper-Pearson 区间而非简单正态近似，公式为 [p̂/(1+z²/n) ± z*sqrt(p̂(1-p̂)/n + z²/4n²)] / (1+z²/n)，以解决小样本下边界越界问题。

## Corrected Claim

CTR 置信区间构造：采用 Wilson 区间或 Clopper-Pearson 区间而非简单正态近似，公式为 [p̂/(1+z²/n) ± z*sqrt(p̂(1-p̂)/n + z²/4n²)] / (1+z²/n)，以解决小样本下边界越界问题。

## Evidence

先验知识/题面给定，逻辑校验通过：Wilson 区间公式推导正确，且确实优于正态近似在处理小样本及边界越界问题上的表现。

## Search Query

Wilson score interval vs normal approximation CTR confidence interval
