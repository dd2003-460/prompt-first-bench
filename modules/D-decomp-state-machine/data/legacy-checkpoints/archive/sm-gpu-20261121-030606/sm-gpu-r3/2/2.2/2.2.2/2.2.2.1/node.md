# N226: W4A16精度下Qwen3-27B在HumanEval基准上的Pass@1得分下降幅度约为2.5%至4.0%（基于Llama-3-70B及Mistral-7B在

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N103, N104, N105

## Claim

W4A16精度下Qwen3-27B在HumanEval基准上的Pass@1得分下降幅度约为2.5%至4.0%（基于Llama-3-70B及Mistral-7B在W4A16下的公开评测数据外推），显著高于FP8的<0.5%损失，需标记为[待核验]以确认Qwen3-27B特定模型的实际表现。

## Corrected Claim

W4A16精度下Qwen3-27B在HumanEval基准上的Pass@1得分预计会有显著下降（参考同类模型外推约为2.5%至4.0%），显著高于FP8的<0.5%损失，具体数值需实测确认。

## Evidence

[质询]该陈述明确标注为基于其他模型（Llama-3-70B, Mistral-7B）的外推，且自标[待核验]，缺乏Qwen3-27B在W4A16下的直接实测数据支持，属于未经证实的经验性推测。 | 先验知识/题面给定，逻辑校验通过（W4A16精度损失通常高于FP8，量级合理），但作为经验事实且无直接来源支持，依据规则降级。

## Search Query

Qwen3-27B W4A16 quantization HumanEval benchmark score drop
