# N131: Qwen3-27B 的 config.json 中 `hidden_size` 为 4096，`num_hidden_layers` 为 48，`num_att

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Qwen3-27B 的 config.json 中 `hidden_size` 为 4096，`num_hidden_layers` 为 48，`num_attention_heads` 为 32，`num_key_value_heads` 为 8，`intermediate_size` 为 11008，`vocab_size` 为 151936。

## Corrected Claim

Qwen3-27B 的 config.json 中 `hidden_size` 为 4096，`num_hidden_layers` 为 48，`num_attention_heads` 为 32，`num_key_value_heads` 为 8，`intermediate_size` 为 11008，`vocab_size` 为 151936。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json hidden_size num_hidden_layers vocab_size
