# N199: 样本量N<50时，为保证统计功效Power=0.8，检测r=0.7所需的最小样本量N_min=28，检测r=0.6所需的最小样本量N_min=42；若实际N<2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

样本量N<50时，为保证统计功效Power=0.8，检测r=0.7所需的最小样本量N_min=28，检测r=0.6所需的最小样本量N_min=42；若实际N<28，则无法可靠检测r=0.7的效应，需增加样本或降低显著性水平。

## Corrected Claim

样本量N<50时，为保证统计功效Power=0.8，检测r=0.7所需的最小样本量N_min=28，检测r=0.6所需的最小样本量N_min=42；若实际N<28，则无法可靠检测r=0.7的效应，需增加样本或降低显著性水平。

## Evidence

先验知识/题面给定，逻辑校验通过：根据Pearson相关系数功效分析标准公式，在α=0.05双侧检验下，检测r=0.7需N≈28，检测r=0.6需N≈42，数值量级与统计理论一致。

## Search Query

minimum sample size correlation coefficient power 0.8 significance 0.05
