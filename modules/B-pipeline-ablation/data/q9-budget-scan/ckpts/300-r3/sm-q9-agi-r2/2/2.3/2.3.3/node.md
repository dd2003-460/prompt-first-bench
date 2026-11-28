# N61: 定义confidence_score的更新机制：初始值0.5，每次被引用且结论验证成功后 +0.1，验证失败 -0.2，设上下界[0,1]，当score < 0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

定义confidence_score的更新机制：初始值0.5，每次被引用且结论验证成功后 +0.1，验证失败 -0.2，设上下界[0,1]，当score < 0.3时标记为低置信并降低检索优先级

## Corrected Claim

定义confidence_score的更新机制：初始值0.5，每次被引用且结论验证成功后 +0.1，验证失败 -0.2，设上下界[0,1]，当score < 0.3时标记为低置信并降低检索优先级

## Evidence

先验知识/题面给定，逻辑校验通过
