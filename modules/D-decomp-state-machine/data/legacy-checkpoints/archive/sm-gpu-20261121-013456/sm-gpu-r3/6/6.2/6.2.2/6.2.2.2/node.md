# N251: Qwen3-27B 的 KV Cache 每 Token 显存占用公式：KV_Cache_Size = 2 * Num_Layers * Num_KV_Head

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

Qwen3-27B 的 KV Cache 每 Token 显存占用公式：KV_Cache_Size = 2 * Num_Layers * Num_KV_Heads * Head_Dim * Bytes_Per_Elem，需代入 Qwen3-27B 的具体架构参数（如 64 layers, 8 KV heads, 128 head_dim）计算 FP16/FP8 下的单 Token 开销。

## Corrected Claim

Qwen3-27B 的 KV Cache 每 Token 显存占用公式：KV_Cache_Size = 2 * Num_Layers * Num_KV_Heads * Head_Dim * Bytes_Per_Elem，需代入 Qwen3-27B 的具体架构参数（如 64 layers, 8 KV heads, 128 head_dim）计算 FP16/FP8 下的单 Token 开销。

## Evidence

先验知识/题面给定，逻辑校验通过
