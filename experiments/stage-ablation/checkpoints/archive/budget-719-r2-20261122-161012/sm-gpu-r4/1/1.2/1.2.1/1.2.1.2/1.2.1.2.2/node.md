# N351: Qwen3-27B 的单层 KV Cache 大小公式为 KV_Layer = 2 * num_kv_heads * head_dim * dtype_byte

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N145

## Claim

Qwen3-27B 的单层 KV Cache 大小公式为 KV_Layer = 2 * num_kv_heads * head_dim * dtype_bytes * seq_len；在 BF16 精度下，每 token 每层占用 2 * 8 * 128 * 2 = 4096 bytes (4 KB)，此值用于后续乘以层数计算总量

## Corrected Claim

Qwen3-27B 的单层 KV Cache 大小公式为 KV_Layer = 2 * num_kv_heads * head_dim * dtype_bytes * seq_len；在 BF16 精度下，每 token 每层占用 2 * 8 * 128 * 2 = 4096 bytes (4 KB)，此值用于后续乘以层数计算总量

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 采用 GQA 架构，num_kv_heads=8, head_dim=128, BF16 精度下每 token 每层 KV 占用 2(K+V) * 8 * 128 * 2 = 4096 bytes，计算无误。
