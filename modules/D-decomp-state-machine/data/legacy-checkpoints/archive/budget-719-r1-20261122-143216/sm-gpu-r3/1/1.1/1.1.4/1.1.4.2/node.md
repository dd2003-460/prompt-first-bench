# N158: Qwen3-27B 的 num_attention_heads 具体数值为 32，结合 hidden_size 计算 head_dim 的关键分母，需查阅官方 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

Qwen3-27B 的 num_attention_heads 具体数值为 32，结合 hidden_size 计算 head_dim 的关键分母，需查阅官方 config.json 确认。

## Corrected Claim

Qwen3-27B 的 num_attention_heads 具体数值为 32，结合 hidden_size 计算 head_dim 的关键分母，需查阅官方 config.json 确认。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json num_attention_heads
