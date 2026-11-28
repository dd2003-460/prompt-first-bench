# N196: 误报率约束条件：FP_rate = (False_Hits / Total_Negative_Samples) * 100% < 5%，其中 False_Hit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

误报率约束条件：FP_rate = (False_Hits / Total_Negative_Samples) * 100% < 5%，其中 False_Hits 指被标记为敏感但实际无害的实验描述，需构建包含 500 条无害科研术语的阴性对照集进行基准测试

## Corrected Claim

误报率约束条件：FP_rate = (False_Hits / Total_Negative_Samples) * 100% < 5%，其中 False_Hits 指被标记为敏感但实际无害的实验描述，需构建包含 500 条无害科研术语的阴性对照集进行基准测试

## Evidence

先验知识/题面给定，逻辑校验通过
