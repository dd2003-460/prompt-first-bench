# N130: Qwen3.8-27B (GQA, 32 heads, 8 KV heads, head_dim=128) 每 token 的 KV Cache 占用量计算：2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Qwen3.8-27B (GQA, 32 heads, 8 KV heads, head_dim=128) 每 token 的 KV Cache 占用量计算：2 (K/V) * 8 (kv_heads) * 128 (dim) * 1 (byte for FP8) = 2048 bytes = 2KB/token。

## Corrected Claim

Qwen3.8-27B (GQA, 32 heads, 8 KV heads, head_dim=128) 每 token 的 KV Cache 占用量计算：2 (K/V) * 8 (kv_heads) * 128 (dim) * 1 (byte for FP8) = 2048 bytes = 2KB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小计算公式为 2(K/V) × num_kv_heads × head_dim × bytes_per_element，代入数值 2×8×128×1=2048 bytes，量纲与数值均正确。

## Search Query

Qwen3.8-27B GQA kv heads dim fp8 kv cache size per token
