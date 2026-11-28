# N123: Causal Inference Bias < 0.1 的量化定义：Bias = |Estimated_Causal_Effect - Ground_Truth

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

Causal Inference Bias < 0.1 的量化定义：Bias = |Estimated_Causal_Effect - Ground_Truth_Causal_Effect| / Ground_Truth_Causal_Effect，需在至少 5 个具有已知因果图结构的合成数据集上验证，若平均相对偏差 > 0.1 则判定失败 [待核验]

## Corrected Claim

Causal Inference Bias < 0.1 的量化定义：Bias = |Estimated_Causal_Effect - Ground_Truth_Causal_Effect| / Ground_Truth_Causal_Effect，需在至少 5 个具有已知因果图结构的合成数据集上验证，若平均相对偏差 > 0.1 则判定失败 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

causal inference bias metric LLM synthetic dataset ground truth
