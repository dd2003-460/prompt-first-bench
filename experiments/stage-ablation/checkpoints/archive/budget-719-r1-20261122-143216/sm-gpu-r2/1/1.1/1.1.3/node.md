# N38: Qwen3-27B 的 num_kv_heads（KV 头数）具体数值，GQA 架构下通常小于 num_attention_heads，需从 config.js

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 的 num_kv_heads（KV 头数）具体数值，GQA 架构下通常小于 num_attention_heads，需从 config.json 获取精确值以计算 KV Cache 大小。

## Corrected Claim

Qwen3-27B 采用 GQA 架构，其 num_kv_heads 通常小于 num_attention_heads，具体数值需查阅官方 config.json 以计算 KV Cache 大小。

## Evidence

[质询]该陈述包含具体经验参数（Qwen3-27B 的 num_kv_heads 具体数值），属于经验事实，无法从第一性原理推导，且当前无可用来源支持其具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B num_kv_heads GQA architecture config.json
