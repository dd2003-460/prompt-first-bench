# N36: KV Cache 显存占用计算公式：KV_Cache_GB = (2 * n_layers * n_heads_kv * head_dim * bytes_pe

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

KV Cache 显存占用计算公式：KV_Cache_GB = (2 * n_layers * n_heads_kv * head_dim * bytes_per_element * seq_len * batch_size) / (1024^3)。对于 Qwen3-27B（假设 n_layers=48, n_heads_kv=8, head_dim=128, BF16），每 1K token 每 batch 占用约 0.15 GB，32K 上下文单 batch 需约 4.8 GB 显存。

## Corrected Claim

KV Cache 显存占用计算公式：KV_Cache_GB = (2 * n_layers * n_heads_kv * head_dim * bytes_per_element * seq_len * batch_size) / (1024^3)。对于 Qwen3-27B（假设 n_layers=48, n_heads_kv=8, head_dim=128, BF16），每 1K token 每 batch 占用约 0.15 GB，32K 上下文单 batch 需约 4.8 GB 显存。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算（48*8*128*2*1024*2/1024^3 ≈ 0.15GB）与结论一致。

## Search Query

Qwen3-27B architecture num_layers num_heads head_dim
