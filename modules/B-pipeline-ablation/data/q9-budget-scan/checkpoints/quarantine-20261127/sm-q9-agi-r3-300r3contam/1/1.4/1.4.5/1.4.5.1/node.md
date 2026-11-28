# N122: Statistical Correctness 100% 要求的现实可行性修正：在有限样本量 n=100 下，即使真实错误率为 0.1%，观察到 0 错误的概率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

Statistical Correctness 100% 要求的现实可行性修正：在有限样本量 n=100 下，即使真实错误率为 0.1%，观察到 0 错误的概率仅为 e^(-0.1) ≈ 90.5%，因此 '100%' 在统计上不可达，应修正为 95% 置信区间下限 > 99.5% 作为操作化标准 [待核验]

## Corrected Claim

Statistical Correctness 100% 要求的现实可行性修正：在有限样本量 n=100 下，即使真实错误率为 0.1%，观察到 0 错误的概率仅为 e^(-0.1) ≈ 90.5%，因此 '100%' 在统计上不可达，应修正为 95% 置信区间下限 > 99.5% 作为操作化标准 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：泊松分布计算 P(X=0)=e^(-λ) 正确，统计推断逻辑自洽

## Search Query

statistical correctness threshold binary outcome sample size confidence interval
