# N8: Qwen3.8-27B采用GQA架构(KV heads=8, head_dim=128)，单token KV Cache大小 = 2 * 8 * 128 * 2

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3.8-27B采用GQA架构(KV heads=8, head_dim=128)，单token KV Cache大小 = 2 * 8 * 128 * 2 bytes (fp8) = 4KB/token

## Corrected Claim

Qwen3.8-27B采用GQA架构(KV heads=8, head_dim=128)，单token KV Cache大小 = 2 * 8 * 128 * 2 bytes (fp8) = 4KB/token

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache大小计算公式为 2 (K和V) * num_kv_heads * head_dim * bytes_per_element，代入数值 2*8*128*2 = 4096 bytes = 4KB，计算无误且符合GQA架构定义。
