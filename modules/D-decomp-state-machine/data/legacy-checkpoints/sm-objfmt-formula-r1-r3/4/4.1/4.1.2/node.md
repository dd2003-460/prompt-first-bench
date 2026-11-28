# N78: Qwen3-27B 的 Key/Value Head 维度 (kv_head_dim) 确认为 128，用于计算单层单 Token 的 KV 字节数

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

Qwen3-27B 的 Key/Value Head 维度 (kv_head_dim) 确认为 128，用于计算单层单 Token 的 KV 字节数

## Corrected Claim

Qwen3-27B 的 Key/Value Head 维度 (kv_head_dim) 通常为 128，用于计算单层单 Token 的 KV 字节数

## Evidence

[质询]缺乏外部来源直接确认 Qwen3-27B 的具体架构参数，且不同模型版本或变体可能存在差异，存在将通用配置误认为特定版本配置的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json head_dim num_key_value_heads
