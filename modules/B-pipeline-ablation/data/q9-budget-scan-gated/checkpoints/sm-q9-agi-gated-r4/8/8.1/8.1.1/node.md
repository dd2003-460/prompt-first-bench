# N140: KV Cache 每 Token 显存占用公式展开：2(K+V) * num_layers(32) * num_kv_heads(8) * head_dim(1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

KV Cache 每 Token 显存占用公式展开：2(K+V) * num_layers(32) * num_kv_heads(8) * head_dim(128) * bytes_per_element(1 FP8) = 64 KB/token；N71 声称的 2KB/token 错误地忽略了层数累加，导致后续并发计算偏差 32 倍。

## Corrected Claim

KV Cache 每 Token 显存占用公式展开：2(K+V) * num_layers(32) * num_kv_heads(8) * head_dim(128) * bytes_per_element(1 FP8) = 64 KB/token；N71 声称的 2KB/token 错误地忽略了层数累加，导致后续并发计算偏差 32 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 32 * 8 * 128 * 1 = 65536 Bytes = 64 KB，计算无误；N71 的 2KB 确实遗漏了层数因子 32，导致 32 倍偏差。
