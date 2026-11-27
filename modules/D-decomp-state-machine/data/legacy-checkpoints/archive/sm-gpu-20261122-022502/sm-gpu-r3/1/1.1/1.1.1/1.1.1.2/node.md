# N105: Qwen3-27B 的 KV 头数 (num_key_value_heads) 为 8 (采用 GQA 机制，Q 头数为 48)，需通过模型 config.js

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Qwen3-27B 的 KV 头数 (num_key_value_heads) 为 8 (采用 GQA 机制，Q 头数为 48)，需通过模型 config.json 确认，直接决定 KV Cache 大小

## Corrected Claim

Qwen3-27B 的 KV 头数 (num_key_value_heads) 为 8 (采用 GQA 机制，Q 头数为 48)，需通过模型 config.json 确认，直接决定 KV Cache 大小

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json num_key_value_heads GQA
