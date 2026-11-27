# N249: GSM8K基准测试中，Qwen3-27B从BF16到INT8的相对性能损失率 = (Score_BF16 - Score_INT8) / Score_BF16，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N109

## Claim

GSM8K基准测试中，Qwen3-27B从BF16到INT8的相对性能损失率 = (Score_BF16 - Score_INT8) / Score_BF16，若基准为82.1%且INT8为80.2%，则损失率为2.31%；若基准修正为80.0%且INT8为78.5%，则损失率为1.88%，该差异影响精度选择决策

## Corrected Claim

GSM8K基准测试中，Qwen3-27B从BF16到INT8的相对性能损失率 = (Score_BF16 - Score_INT8) / Score_BF16，若基准为82.1%且INT8为80.2%，则损失率为2.31%；若基准修正为80.0%且INT8为78.5%，则损失率为1.88%，该差异影响精度选择决策

## Evidence

先验知识/题面给定，逻辑校验通过：(82.1-80.2)/82.1≈2.31%，(80.0-78.5)/80.0=1.875%≈1.88%，计算无误且逻辑自洽
