# N126: Qwen3-27B 的 num_kv_heads（KV 头数）具体数值，需从 HuggingFace 官方模型卡 config.json 中检索，若采用 GQA

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

Qwen3-27B 的 num_kv_heads（KV 头数）具体数值，需从 HuggingFace 官方模型卡 config.json 中检索，若采用 GQA 架构，此值应显著小于 num_attention_heads，直接影响 KV Cache 大小。

## Corrected Claim

Qwen3-27B 采用 GQA 架构，其 num_kv_heads 显著小于 num_attention_heads，具体数值需查阅 HuggingFace 官方模型卡 config.json 确认。

## Evidence

[质询]该陈述包含具体的经验事实（Qwen3-27B 的 num_kv_heads 具体数值），但参考来源为空，无法通过外部检索直接验证该具体数值是否准确，存在数值错误的可能性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json num_kv_heads
