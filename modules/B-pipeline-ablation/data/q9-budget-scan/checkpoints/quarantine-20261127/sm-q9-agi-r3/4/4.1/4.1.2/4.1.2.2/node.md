# N179: Qwen3.8-27B 在 FP16 KV Cache 模式下，单 Token 的 KV 显存占用量为 131,072 Bytes (128 KB)，计算公式为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

Qwen3.8-27B 在 FP16 KV Cache 模式下，单 Token 的 KV 显存占用量为 131,072 Bytes (128 KB)，计算公式为 2 (K+V) * 32 (layers) * 8 (kv_heads) * 128 (dim) * 2 (bytes)，是 FP8 模式的 2 倍。

## Corrected Claim

Qwen3.8-27B 在 FP16 KV Cache 模式下，单 Token 的 KV 显存占用量为 131,072 Bytes (128 KB)，计算公式为 2 (K+V) * 32 (layers) * 8 (kv_heads) * 128 (dim) * 2 (bytes)，是 FP8 模式的 2 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：计算公式 2*32*8*128*2 = 131,072 Bytes 数学正确，且 FP16 字节数为 FP8 的 2 倍符合数据类型位宽常识。
