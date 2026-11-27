# N157: Qwen3-27B 的 KV Cache 每 token 显存占用公式展开：Bytes_per_token = 2 (K+V) × Num_Layers × N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

Qwen3-27B 的 KV Cache 每 token 显存占用公式展开：Bytes_per_token = 2 (K+V) × Num_Layers × Num_KV_Heads × Head_Dim × Bytes_per_element。

## Corrected Claim

Qwen3-27B 的 KV Cache 每 token 显存占用公式展开：Bytes_per_token = 2 (K+V) × Num_Layers × Num_KV_Heads × Head_Dim × Bytes_per_element。

## Evidence

先验知识/题面给定，逻辑校验通过
