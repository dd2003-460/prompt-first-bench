# N158: Qwen3-27B 的注意力头配置：num_attention_heads=32, num_key_value_heads=8 (GQA 4:1), head_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

Qwen3-27B 的注意力头配置：num_attention_heads=32, num_key_value_heads=8 (GQA 4:1), head_dim=128，此配置决定了 KV Cache 的维度为 8*128=1024 per layer per token

## Corrected Claim

Qwen3-27B 的注意力头配置：num_attention_heads=32, num_key_value_heads=8 (GQA 4:1), head_dim=128，此配置决定了 KV Cache 的维度为 8*128=1024 per layer per token

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数符合公开技术报告，KV Cache 维度计算 (8 heads * 128 dim) 逻辑自洽。
