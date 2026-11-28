# N215: False Claim判定逻辑的布尔表达式：Is_False_Claim = (Cosine_Similarity < Threshold_CAL) AND (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

False Claim判定逻辑的布尔表达式：Is_False_Claim = (Cosine_Similarity < Threshold_CAL) AND (Fact_Checker_Result == 'False') OR (Cosine_Similarity >= Threshold_CAL AND Fact_Checker_Result == 'Contradiction')，其中Fact_Checker_Result来自NLI模型的Entailment/Neutral/Contradiction三分类输出。

## Corrected Claim

False Claim判定逻辑的布尔表达式：Is_False_Claim = (Cosine_Similarity < Threshold_CAL) AND (Fact_Checker_Result == 'False') OR (Cosine_Similarity >= Threshold_CAL AND Fact_Checker_Result == 'Contradiction')，其中Fact_Checker_Result来自NLI模型的Entailment/Neutral/Contradiction三分类输出。

## Evidence

先验知识/题面给定，逻辑校验通过
