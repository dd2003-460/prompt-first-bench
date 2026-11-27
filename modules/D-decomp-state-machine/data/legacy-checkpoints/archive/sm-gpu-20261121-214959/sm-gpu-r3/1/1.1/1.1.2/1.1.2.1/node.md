# N136: Qwen3-27B 的 GQA 组数（Grouping Factor）为 4，计算式为 num_attention_heads(32) / num_key_va

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Qwen3-27B 的 GQA 组数（Grouping Factor）为 4，计算式为 num_attention_heads(32) / num_key_value_heads(8) = 4，此参数决定了 KV Cache 的空间压缩比相对于 MHA 为 1/4。

## Corrected Claim

Qwen3-27B 的 GQA 组数（Grouping Factor）为 4，计算式为 num_attention_heads(32) / num_key_value_heads(8) = 4，此参数决定了 KV Cache 的空间压缩比相对于 MHA 为 1/4。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 确实采用 GQA 架构，其 num_attention_heads 为 32，num_key_value_heads 为 8，组数计算 32/8=4 正确，KV Cache 压缩比 1/4 符合 GQA 原理。
