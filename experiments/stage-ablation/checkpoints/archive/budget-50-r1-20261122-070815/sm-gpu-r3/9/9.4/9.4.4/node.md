# N415: Pass@k (k>1) 口径下的得分差异：在 GSM8K 这类多步推理任务中，INT4 量化导致的逻辑错误可能在 Pass@1 中表现为小幅下降，但在 Pas

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N144

## Claim

Pass@k (k>1) 口径下的得分差异：在 GSM8K 这类多步推理任务中，INT4 量化导致的逻辑错误可能在 Pass@1 中表现为小幅下降，但在 Pass@10 中因采样多样性增加而收敛至 BF16 水平；需获取 Qwen3-27B 在 Pass@10 口径下 BF16 与 INT4 的得分以验证此效应。

## Corrected Claim

在 GSM8K 等多步推理任务中，INT4 量化导致的逻辑错误可能在 Pass@1 中表现为小幅下降，但在 Pass@10 中可能因采样多样性增加而显著收敛；需获取 Qwen3-27B 在 Pass@10 口径下 BF16 与 INT4 的得分以验证此效应。

## Evidence

[质询]该陈述包含具体的经验性预测（INT4在Pass@10下收敛至BF16水平）和特定模型（Qwen3-27B）的数据需求，属于经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B GSM8K Pass@10 BF16 vs INT4 quantization degradation
