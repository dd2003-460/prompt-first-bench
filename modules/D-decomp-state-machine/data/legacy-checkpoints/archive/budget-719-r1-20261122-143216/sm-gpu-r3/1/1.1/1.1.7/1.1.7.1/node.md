# N168: Qwen3-27B 的 head_dim 精确值为 128，来源为 HuggingFace Qwen/Qwen3-27B 模型仓库的 config.json 文

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N42, N43, N50

## Claim

Qwen3-27B 的 head_dim 精确值为 128，来源为 HuggingFace Qwen/Qwen3-27B 模型仓库的 config.json 文件中的 'hidden_size' (8192) 除以 'num_attention_heads' (64) 得出。

## Corrected Claim

Qwen3-27B 的 head_dim 计算方式为 hidden_size 除以 num_attention_heads，若配置为 8192 和 64，则 head_dim 为 128。

## Evidence

[质询]该陈述包含具体的经验参数（hidden_size=8192, num_attention_heads=64），属于模型配置细节，无法从第一性原理推导，且当前无可用外部来源直接验证这些具体数值是否准确。 | 经验事实，逻辑自洽（8192/64=128）但缺来源支持，且检索通道失败无法外部核验。

## Search Query

Qwen3-27B config.json hidden_size num_attention_heads
