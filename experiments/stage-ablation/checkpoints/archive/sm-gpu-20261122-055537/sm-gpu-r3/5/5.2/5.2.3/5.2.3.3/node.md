# N278: 量化损失的可接受性阈值定义：若业务场景为通用问答 (Q_score 权重高)，INT4 的 2-3% MMLU 下降可接受 (Q_score > 0.95)；若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

量化损失的可接受性阈值定义：若业务场景为通用问答 (Q_score 权重高)，INT4 的 2-3% MMLU 下降可接受 (Q_score > 0.95)；若业务场景为代码辅助 (HumanEval 权重高)，INT4 的 4-8% 下降可能导致 Q_score < 0.90，此时需评估是否回退至 INT8 或 FP8 以换取 <1% 的损失。

## Corrected Claim

量化损失的可接受性阈值定义：若业务场景为通用问答 (Q_score 权重高)，INT4 的 2-3% MMLU 下降可接受 (Q_score > 0.95)；若业务场景为代码辅助 (HumanEval 权重高)，INT4 的 4-8% 下降可能导致 Q_score < 0.90，此时需评估是否回退至 INT8 或 FP8 以换取 <1% 的损失。

## Evidence

先验知识/题面给定，逻辑校验通过
