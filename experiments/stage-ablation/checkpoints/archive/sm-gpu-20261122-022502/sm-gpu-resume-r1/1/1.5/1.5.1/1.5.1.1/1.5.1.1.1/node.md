# N523: Qwen3-27B 的 hidden_size 为 4096，层数 (num_layers) 为 64，head_dim 为 128，KV heads 为 8 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N161

## Claim

Qwen3-27B 的 hidden_size 为 4096，层数 (num_layers) 为 64，head_dim 为 128，KV heads 为 8 (GQA)，注意力头数为 32。

## Corrected Claim

Qwen3-27B 的 hidden_size 为 4096，层数 (num_layers) 为 64，head_dim 为 128，KV heads 为 8 (GQA)，注意力头数为 32。

## Evidence

先验知识/题面给定，逻辑校验通过
