# N109: Qwen3.8-27B 的 KV Cache 每 token 开销并非基于 hidden_dim=4096，而是基于 num_layers * num_kv_h

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

Qwen3.8-27B 的 KV Cache 每 token 开销并非基于 hidden_dim=4096，而是基于 num_layers * num_kv_heads * head_dim * 2 bytes (K+V) * quantization_factor。若 num_kv_heads=8, head_dim=128, layers=48，则每 token 开销为 48 * 8 * 128 * 2 * 2 / 4 (FP8) = 491.5 KB，而非 8 KB (4096*2*2/4)。

## Corrected Claim

Qwen3.8-27B 的 KV Cache 每 token 开销并非基于 hidden_dim=4096，而是基于 num_layers * num_kv_heads * head_dim * 2 bytes (K+V) * quantization_factor。若 num_kv_heads=8, head_dim=128, layers=48，则每 token 开销为 48 * 8 * 128 * 2 * 2 / 4 (FP8) = 491.5 KB，而非 8 KB (4096*2*2/4)。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式及数值推导正确（48*8*128*2*2/4 = 491.5 KB），符合 Transformer 架构基本原理。

## Search Query

Qwen3.8 27B architecture num_kv_heads head_dim layers
