# N54: 报告生成的最小必要字段集合 (JSON Schema) 必须包含：test_type, statistic_value, degrees_of_freedom,

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

报告生成的最小必要字段集合 (JSON Schema) 必须包含：test_type, statistic_value, degrees_of_freedom, p_value, effect_size_value, confidence_interval [lower, upper], n_samples_per_group; 缺失任一字段则判定为 'Incomplete Report' 并触发重试。

## Corrected Claim

报告生成的最小必要字段集合 (JSON Schema) 必须包含：test_type, statistic_value, degrees_of_freedom, p_value, effect_size_value, confidence_interval [lower, upper], n_samples_per_group; 缺失任一字段则判定为 'Incomplete Report' 并触发重试。

## Evidence

先验知识/题面给定，逻辑校验通过
