# N95: Qwen3-27B 的 Transformer 架构参数为：64 层 (num_layers=64)，GQA 配置下 KV 头数 (num_kv_heads) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

Qwen3-27B 的 Transformer 架构参数为：64 层 (num_layers=64)，GQA 配置下 KV 头数 (num_kv_heads) 为 8，头维度 (head_dim) 为 128。

## Corrected Claim

Qwen3-27B 的 Transformer 架构参数为：64 层 (num_layers=64)，GQA 配置下 KV 头数 (num_kv_heads) 为 8，头维度 (head_dim) 为 128。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json num_layers num_key_value_heads head_dim
