# N186: Qwen3-27B 在 W4 量化下的实际 KV Cache 每 Token 占用量：基于 GQA 架构，假设 num_kv_heads = 8, head_d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

Qwen3-27B 在 W4 量化下的实际 KV Cache 每 Token 占用量：基于 GQA 架构，假设 num_kv_heads = 8, head_dim = 128, num_layers = 64，则每 Token KV Cache 大小 = 2 * 8 * 128 * 64 * 1 byte (FP16/INT8) ≈ 128 KB/Token，若使用 FP8 KV Cache 则为 64 KB/Token

## Corrected Claim

Qwen3-27B 在 W4 量化下的实际 KV Cache 每 Token 占用量：基于 GQA 架构，假设 num_kv_heads = 8, head_dim = 128, num_layers = 64，则每 Token KV Cache 大小 = 2 * 8 * 128 * 64 * 1 byte (FP16/INT8) ≈ 128 KB/Token，若使用 FP8 KV Cache 则为 64 KB/Token

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2(K/V) * 8(heads) * 128(dim) * 64(layers) * 1(byte) = 131,072 bytes = 128 KB，数值量级与算术逻辑均正确。
