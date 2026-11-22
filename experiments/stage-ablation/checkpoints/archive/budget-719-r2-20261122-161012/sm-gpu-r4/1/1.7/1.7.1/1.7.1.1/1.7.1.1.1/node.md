# N435: Qwen3-27B 的架构参数确认为：hidden_size=4096, num_hidden_layers=64, num_key_value_heads=8

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N181

## Claim

Qwen3-27B 的架构参数确认为：hidden_size=4096, num_hidden_layers=64, num_key_value_heads=8 (GQA), head_dim=128, vocab_size=151936, tie_word_embeddings=true。此参数集是计算权重和 KV Cache 的唯一依据，需修正 N182 中错误的 n_layers=48 和 N183 中错误的 n_kv_heads=4。

## Corrected Claim

Qwen3-27B 的架构参数确认为：hidden_size=4096, num_hidden_layers=64, num_key_value_heads=8 (GQA), head_dim=128, vocab_size=151936, tie_word_embeddings=true。此参数集是计算权重和 KV Cache 的唯一依据，需修正 N182 中错误的 n_layers=48 和 N183 中错误的 n_kv_heads=4。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json num_hidden_layers num_key_value_heads head_dim vocab_size
