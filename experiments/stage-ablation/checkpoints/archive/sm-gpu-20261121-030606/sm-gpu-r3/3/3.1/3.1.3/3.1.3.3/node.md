# N252: HumanEval基准测试中，Qwen3-27B从BF16到INT8的相对性能损失率 = (Score_BF16 - Score_INT8) / Score_B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N110

## Claim

HumanEval基准测试中，Qwen3-27B从BF16到INT8的相对性能损失率 = (Score_BF16 - Score_INT8) / Score_BF16，若基准为68.5%且INT8为66.1%，则损失率为3.50%；该损失率需与代码应用场景的质量容忍阈值（通常<2%）对比以判断INT8可行性

## Corrected Claim

HumanEval基准测试中，Qwen3-27B从BF16到INT8的相对性能损失率 = (Score_BF16 - Score_INT8) / Score_BF16，若基准为68.5%且INT8为66.1%，则损失率为3.50%；该损失率需与代码应用场景的质量容忍阈值（通常<2%）对比以判断INT8可行性

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 (68.5-66.1)/68.5 ≈ 3.50% 正确，且量化损失与阈值对比的逻辑框架自洽。
