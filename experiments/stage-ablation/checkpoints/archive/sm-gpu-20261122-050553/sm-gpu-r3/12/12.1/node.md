# N341: ETPD 公式中 Quality_Score 的量化定义：Quality_Score = 0.6 * (MMLU_score_quantized / MMLU_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N118

## Claim

ETPD 公式中 Quality_Score 的量化定义：Quality_Score = 0.6 * (MMLU_score_quantized / MMLU_score_BF16) + 0.4 * (HumanEval_pass_rate_quantized / HumanEval_pass_rate_BF16)，权重 0.6/0.4 基于 Qwen3 官方评测中通用知识与代码生成能力的相对重要性设定 [待核验]，确保分数归一化至 [0,1] 区间。

## Corrected Claim

ETPD 公式中 Quality_Score 通常定义为 MMLU 相对分数与 HumanEval 相对分数的加权平均，权重系数（如 0.6/0.4）依据具体评测场景对通用知识与代码能力的侧重而设定，确保分数归一化至 [0,1] 区间。

## Evidence

[质询]权重 0.6/0.4 的具体数值设定缺乏公开权威来源支持，属于特定模型或内部评测的主观经验参数，无法从第一性原理推导，且存在将特定场景权重泛化为通用定义的风险。 | source=knowledge，公式结构逻辑自洽且归一化区间合理，但具体权重系数属于经验事实，缺乏外部来源直接支持，依据经验事实排除条款降级。
