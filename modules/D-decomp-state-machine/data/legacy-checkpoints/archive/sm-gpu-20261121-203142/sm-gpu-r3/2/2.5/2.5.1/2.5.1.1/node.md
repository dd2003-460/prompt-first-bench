# N201: 质量可接受性综合判定公式：Acceptance_Score = w1 * (1 - ΔMMLU/2.0%) + w2 * (1 - ΔGPQA/3.0%) + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N63

## Claim

质量可接受性综合判定公式：Acceptance_Score = w1 * (1 - ΔMMLU/2.0%) + w2 * (1 - ΔGPQA/3.0%) + w3 * (1 - ΔHumanEval/5.0%)，其中 w1, w2, w3 为业务场景权重，需根据用户是否关注代码生成设定 [待核验]

## Corrected Claim

质量可接受性综合判定公式：Acceptance_Score = w1 * (1 - ΔMMLU/2.0%) + w2 * (1 - ΔGPQA/3.0%) + w3 * (1 - ΔHumanEval/5.0%)，其中 w1, w2, w3 为业务场景权重，需根据用户是否关注代码生成设定 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过
