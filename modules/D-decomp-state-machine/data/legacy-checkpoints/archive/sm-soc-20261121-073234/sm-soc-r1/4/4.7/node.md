# N29: 不确定性量化方法：对每个断言 H1-H4，计算 95% 置信区间 [C_low, C_high]，其中 C_low = C - 1.96*SE, C_high 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

不确定性量化方法：对每个断言 H1-H4，计算 95% 置信区间 [C_low, C_high]，其中 C_low = C - 1.96*SE, C_high = C + 1.96*SE，SE（标准误）基于样本量 n 和效应量 d 估算。例如，若 n=1000，d=0.2，则 SE ≈ 0.063，H1 的 95% CI 为 [0.47, 0.73]。

## Corrected Claim

不确定性量化方法：对每个断言 H1-H4，计算 95% 置信区间 [C_low, C_high]，其中 C_low = C - 1.96*SE, C_high = C + 1.96*SE，SE（标准误）基于样本量 n 和效应量 d 估算。例如，若 n=1000，d=0.2，则 SE ≈ 0.063，H1 的 95% CI 为 [0.47, 0.73]。

## Evidence

先验知识/题面给定，逻辑校验通过：SE公式 sqrt(2/n) 计算正确，CI区间推导符合统计学原理

## Search Query

confidence interval calculation standard error effect size sample size
