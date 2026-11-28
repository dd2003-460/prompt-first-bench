# N32: Qwen3-27B 的架构参数：n_layers=64, hidden_size=4096, num_attention_heads=32, num_key_v

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

Qwen3-27B 的架构参数：n_layers=64, hidden_size=4096, num_attention_heads=32, num_key_value_heads=8 (GQA), head_dim=128, intermediate_size=11008。

## Corrected Claim

Qwen3-27B 的架构参数：n_layers=64, hidden_size=4096, num_attention_heads=32, num_key_value_heads=8 (GQA), head_dim=128, intermediate_size=11008。

## Evidence

先验知识/题面给定，逻辑校验通过
