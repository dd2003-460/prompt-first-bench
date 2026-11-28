# N178: Qwen3.8-27B 在 FP8 KV Cache 模式下，单 Token 的 KV 显存占用量为 65,536 Bytes (64 KB)，计算公式为 2 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

Qwen3.8-27B 在 FP8 KV Cache 模式下，单 Token 的 KV 显存占用量为 65,536 Bytes (64 KB)，计算公式为 2 (K+V) * 32 (layers) * 8 (kv_heads) * 128 (dim) * 1 (byte)。

## Corrected Claim

Qwen3.8-27B 在 FP8 KV Cache 模式下，单 Token 的 KV 显存占用量为 65,536 Bytes (64 KB)，计算公式为 2 (K+V) * 32 (layers) * 8 (kv_heads) * 128 (dim) * 1 (byte)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2*32*8*128*1 = 65536 计算正确，符合 Transformer 架构中 KV Cache 显存占用的标准计算逻辑（层数×头数×维度×字节数×2(K/V)）。
