# N375: PPL 相对增加率 Delta_PPL = (PPL_W8A8 - PPL_BF16) / PPL_BF16 * 100%，需计算具体百分比并验证是否 <0.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N132

## Claim

PPL 相对增加率 Delta_PPL = (PPL_W8A8 - PPL_BF16) / PPL_BF16 * 100%，需计算具体百分比并验证是否 <0.5%；若 >0.5%，需标记 [语言建模质量轻微受损] 并评估对长文本生成连贯性的潜在影响。

## Corrected Claim

PPL 相对增加率 Delta_PPL = (PPL_W8A8 - PPL_BF16) / PPL_BF16 * 100%，需计算具体百分比并验证是否 <0.5%；若 >0.5%，需标记 [语言建模质量轻微受损] 并评估对长文本生成连贯性的潜在影响。

## Evidence

先验知识/题面给定，逻辑校验通过
