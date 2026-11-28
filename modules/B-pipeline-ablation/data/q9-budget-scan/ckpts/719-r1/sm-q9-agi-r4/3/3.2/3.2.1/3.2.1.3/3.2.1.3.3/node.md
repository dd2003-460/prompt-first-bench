# N512: 工作点3 下 MTP×4 投机解码在超长序列 (L=262144) 的接受率衰减模型：Acceptance_Rate(L) = Base_Rate × exp(

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N183

## Claim

工作点3 下 MTP×4 投机解码在超长序列 (L=262144) 的接受率衰减模型：Acceptance_Rate(L) = Base_Rate × exp(-α×L)，需估计 α 值以确定在 L=262144 时有效加速比是否降至 1.5x 以下，从而决定是否禁用 MTP

## Corrected Claim

工作点3 下 MTP×4 投机解码在超长序列 (L=262144) 的接受率可能随序列长度增加而下降，具体衰减模型（如指数衰减 Acceptance_Rate(L) = Base_Rate × exp(-α×L)）及参数 α 需通过实验数据拟合确定，以评估有效加速比是否降至 1.5x 以下。

## Evidence

[质询]该陈述假设接受率随序列长度呈指数衰减（exp(-α×L)），这是一个未经证实的经验模型假设。实际上，MTP（Multi-Token Prediction）或投机解码的接受率主要取决于草稿模型与目标模型的分布一致性，以及上下文窗口内的注意力机制影响，并不必然遵循简单的指数衰减规律。此外，α值的估计缺乏具体数据支撑，属于未验证的经验参数。 | 经验事实，逻辑自洽但缺来源支持。该模型形式在数学上可行，但具体衰减机制和α值需实证数据验证，当前无外部来源支持该特定指数模型的有效性。

## Search Query

speculative decoding acceptance rate decay long context length llm inference mtp vllm
