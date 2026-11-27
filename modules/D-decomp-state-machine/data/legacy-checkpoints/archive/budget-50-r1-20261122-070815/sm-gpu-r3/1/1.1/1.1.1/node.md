# N35: Qwen3-27B 的层数 (n_layers) 为 64，KV 头数 (n_kv_heads) 为 4，注意力头维度 (head_dim) 为 128，这些参

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 的层数 (n_layers) 为 64，KV 头数 (n_kv_heads) 为 4，注意力头维度 (head_dim) 为 128，这些参数是计算 KV Cache 的基础输入。

## Corrected Claim

Qwen3-27B 的层数 (n_layers) 为 64，KV 头数 (n_kv_heads) 为 4，注意力头维度 (head_dim) 为 128，这些参数是计算 KV Cache 的基础输入。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json n_layers n_kv_heads head_dim
