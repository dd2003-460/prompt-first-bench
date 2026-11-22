# N272: 策略复杂度系数 k_complexity 取决于算法建议的更新频率 f_update（次/周）与建议偏离卖家直觉定价的比例 d_deviation，公式为 k_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

策略复杂度系数 k_complexity 取决于算法建议的更新频率 f_update（次/周）与建议偏离卖家直觉定价的比例 d_deviation，公式为 k_complexity = f_update * d_deviation * 0.1，当 f_update > 2 且 d_deviation > 0.2 时，k_complexity 显著增加学习成本

## Corrected Claim

策略复杂度系数 k_complexity 取决于算法建议的更新频率 f_update（次/周）与建议偏离卖家直觉定价的比例 d_deviation，公式为 k_complexity = f_update * d_deviation * 0.1，当 f_update > 2 且 d_deviation > 0.2 时，k_complexity 显著增加学习成本

## Evidence

先验知识/题面给定，逻辑校验通过
