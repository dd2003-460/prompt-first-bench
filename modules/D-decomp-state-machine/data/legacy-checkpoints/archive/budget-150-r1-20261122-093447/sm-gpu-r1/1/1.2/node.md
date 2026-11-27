# N8: Qwen3-27B 架构参数：n_layers=64, hidden_size=4096, n_heads=32, n_kv_heads=8, head_dim

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 架构参数：n_layers=64, hidden_size=4096, n_heads=32, n_kv_heads=8, head_dim=128, intermediate_size=11008, vocab_size=152064, tie_word_embeddings=False, rope_theta=1000000, rope_scaling_type='yarn', rope_factor=4.0

## Corrected Claim

Qwen3-27B 架构参数：n_layers=64, hidden_size=4096, n_heads=32, n_kv_heads=8, head_dim=128, intermediate_size=11008, vocab_size=152064, tie_word_embeddings=False, rope_theta=1000000, rope_scaling_type='yarn', rope_factor=4.0

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json n_layers n_kv_heads hidden_size
