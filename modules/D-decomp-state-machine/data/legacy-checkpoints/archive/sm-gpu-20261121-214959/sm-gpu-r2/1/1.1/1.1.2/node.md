# N38: Qwen3-27B 的 KV Cache 头数（num_key_value_heads）为 8 头（采用 Grouped Query Attention, GQ

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7, N8, N9

## Claim

Qwen3-27B 的 KV Cache 头数（num_key_value_heads）为 8 头（采用 Grouped Query Attention, GQA 策略），每头维度（head_dim）为 128 维，总隐藏层维度（hidden_size）为 4096 维。

## Corrected Claim

Qwen3-27B 采用 Grouped Query Attention (GQA) 策略，其 KV Cache 头数（num_key_value_heads）为 8，每头维度（head_dim）为 128，总隐藏层维度（hidden_size）为 4096。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（经验事实），且参考来源全部缺失，无法通过外部检索直接验证其准确性，存在参数记忆偏差或版本混淆的风险。 | 经验事实，逻辑自洽（hidden_size 4096 / head_dim 128 = 32 个 Query 头，GQA 下 8 个 KV 头符合常见比例），但缺来源支持。

## Search Query

Qwen3-27B GQA num_key_value_heads head_dim hidden_size
