# N41: Qwen3-27B 的每个注意力头的维度（head_dim）为 128，计算公式为 hidden_size / num_attention_heads (409

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 的每个注意力头的维度（head_dim）为 128，计算公式为 hidden_size / num_attention_heads (4096/32=128)，用于确定单个 KV 向量的长度。

## Corrected Claim

Qwen3-27B 的每个注意力头的维度（head_dim）通常为 128，计算公式为 hidden_size / num_attention_heads，用于确定单个 KV 向量的长度。

## Evidence

[质询]该陈述包含具体的模型架构参数（hidden_size=4096, num_attention_heads=32），属于经验事实。虽然 Qwen3-27B 确实存在且通常采用此类配置，但在缺乏外部来源直接确认具体数值的情况下，无法排除该特定版本或变体参数不同的可能性（例如某些 MoE 变体或不同尺寸模型参数不同）。 | 经验事实，逻辑自洽（4096/32=128 计算正确，head_dim 定义符合 Transformer 标准），但缺来源支持。

## Search Query

Qwen3-27B config.json head_dim or num_attention_heads
