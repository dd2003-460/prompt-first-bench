# N270: 状态漂移检测阈值 Threshold_Drift 设定为 Levenshtein 距离 D > 10，该阈值基于历史正常波动 P95 值（约 5-8）的 1.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

状态漂移检测阈值 Threshold_Drift 设定为 Levenshtein 距离 D > 10，该阈值基于历史正常波动 P95 值（约 5-8）的 1.5 倍安全边际确定，用于区分正常状态更新与异常逻辑断裂

## Corrected Claim

状态漂移检测阈值 Threshold_Drift 设定为 Levenshtein 距离 D > 10，该阈值基于历史正常波动 P95 值（约 5-8）的 1.5 倍安全边际确定，用于区分正常状态更新与异常逻辑断裂

## Evidence

先验知识/题面给定，逻辑校验通过：Levenshtein距离为整数，P95值5-8的1.5倍约为7.5-12，取整阈值10处于合理区间，符合基于统计分位数设定安全边际的工程惯例。
