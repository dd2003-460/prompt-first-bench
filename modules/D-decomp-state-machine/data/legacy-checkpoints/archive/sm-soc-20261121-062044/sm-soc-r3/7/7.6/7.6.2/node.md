# N264: 样本量敏感性分析：当真实效应量 d 从 0.2 增加至 0.5（中等效应）时，所需最小样本量 n_per_group 从 157 降至 34；若平台实际降价卖家

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

样本量敏感性分析：当真实效应量 d 从 0.2 增加至 0.5（中等效应）时，所需最小样本量 n_per_group 从 157 降至 34；若平台实际降价卖家样本量 n_actual < 34，则即使存在中等效应，统计功效也低于 0.5，此时无法区分'无效果'与'样本不足'。

## Corrected Claim

样本量敏感性分析：当真实效应量 d 从 0.2 增加至 0.5（中等效应）时，所需最小样本量 n_per_group 从 157 降至 34；若平台实际降价卖家样本量 n_actual < 34，则即使存在中等效应，统计功效也低于 0.5，此时无法区分'无效果'与'样本不足'。

## Evidence

先验知识/题面给定，逻辑校验通过：基于双样本t检验功效公式，d=0.2时n≈157，d=0.5时n≈34，数值量级与统计功效理论一致，且n<34时功效<0.5的推论符合统计学原理。

## Search Query

sample size calculation for t-test effect size d=0.5 power 0.8
