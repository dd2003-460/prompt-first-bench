# N183: Qwen3-27B 的 KV Cache 每 token 大小计算公式为：KV_per_token = 2 * num_layers * num_kv_head

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

Qwen3-27B 的 KV Cache 每 token 大小计算公式为：KV_per_token = 2 * num_layers * num_kv_heads * head_dim * bytes_per_element。对于 Qwen3-27B，num_layers=64, num_kv_heads=8 (GQA), head_dim=128, 计算得每层 KV 大小为 2*8*128*bytes。若 BF16 (2 bytes)，每 token KV 为 262,144 bytes (256 KB)；若 FP8 (1 byte)，每 token KV 为 131,072 bytes (128 KB)。

## Corrected Claim

Qwen3-27B 的 KV Cache 每 token 大小计算公式为：KV_per_token = 2 * num_layers * num_kv_heads * head_dim * bytes_per_element。对于 Qwen3-27B，num_layers=64, num_kv_heads=8 (GQA), head_dim=128, 计算得每层 KV 大小为 2*8*128*bytes。若 BF16 (2 bytes)，每 token KV 为 262,144 bytes (256 KB)；若 FP8 (1 byte)，每 token KV 为 131,072 bytes (128 KB)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，GQA下num_kv_heads为8），数值计算准确（64层 * 2 * 8头 * 128维 * 2字节 = 262,144 bytes），符合Qwen3-27B的架构参数。
