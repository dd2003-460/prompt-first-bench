# N39: Qwen3-27B 的 Head Dimension (head_dim) 为 128，结合 num_kv_heads=8，每层每个 token 的 KV Ca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Qwen3-27B 的 Head Dimension (head_dim) 为 128，结合 num_kv_heads=8，每层每个 token 的 KV Cache 占用为 2 (K+V) × 8 (heads) × 128 (dim) × 2 bytes (BF16) = 4096 bytes/token/layer，64层总计 256 KB/token。

## Corrected Claim

Qwen3-27B 的 Head Dimension (head_dim) 为 128，结合 num_kv_heads=8，每层每个 token 的 KV Cache 占用为 2 (K+V) × 8 (heads) × 128 (dim) × 2 bytes (BF16) = 4096 bytes/token/layer，64层总计 256 KB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 8 * 128 * 2 * 64 = 262,144 bytes = 256 KB，数值与逻辑均正确。

## Search Query

Qwen3-27B head_dim 128 KV cache calculation per token
