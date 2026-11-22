# N306: HumanEval 准确率下降幅度 Δ_HumanEval = Pass@1_BF16 - Pass@1_INT4。若 Pass@1_BF16 = 72.5% 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

HumanEval 准确率下降幅度 Δ_HumanEval = Pass@1_BF16 - Pass@1_INT4。若 Pass@1_BF16 = 72.5% (假设中值), Pass@1_INT4 = 65.0% (假设中值), 则 Δ = 7.5 个百分点。Q_score_HumanEval = 65.0 / 72.5 ≈ 0.897。

## Corrected Claim

HumanEval 准确率下降幅度 Δ_HumanEval = Pass@1_BF16 - Pass@1_INT4。若 Pass@1_BF16 = 72.5% (假设中值), Pass@1_INT4 = 65.0% (假设中值), 则 Δ = 7.5 个百分点。Q_score_HumanEval = 65.0 / 72.5 ≈ 0.897。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 72.5 - 65.0 = 7.5 及 65.0 / 72.5 ≈ 0.8965 均正确，量纲一致。
