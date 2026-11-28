# N667: 阈值 T_threshold 的解析解：T_threshold = (Local_HR - Target_HR) / b，其中 Local_HR 为本地 Qwe

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N243

## Claim

阈值 T_threshold 的解析解：T_threshold = (Local_HR - Target_HR) / b，其中 Local_HR 为本地 Qwen3.8-27B 基线幻觉率（假设 0.25），Target_HR 为可接受幻觉率（假设 0.10），b 为回归斜率（假设 0.05/单位 CS），则 T_threshold = (0.25-0.10)/0.05 = 3.0

## Corrected Claim

阈值 T_threshold 的解析解：T_threshold = (Local_HR - Target_HR) / b，其中 Local_HR 为本地 Qwen3.8-27B 基线幻觉率（假设 0.25），Target_HR 为可接受幻觉率（假设 0.10），b 为回归斜率（假设 0.05/单位 CS），则 T_threshold = (0.25-0.10)/0.05 = 3.0

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 (0.25-0.10)/0.05=3.0 正确，公式定义与假设参数一致，无内部矛盾。
