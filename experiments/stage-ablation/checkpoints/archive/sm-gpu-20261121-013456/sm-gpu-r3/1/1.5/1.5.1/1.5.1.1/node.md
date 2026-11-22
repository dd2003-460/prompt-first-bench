# N155: Qwen3-27B 的 KV Cache 每 token 显存占用公式：KV_Cache_per_token = 2 * Num_Layers * Num_KV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

Qwen3-27B 的 KV Cache 每 token 显存占用公式：KV_Cache_per_token = 2 * Num_Layers * Num_KV_Heads * Head_Dim * Bytes_Per_Element，其中 Num_Layers=64, Num_KV_Heads=8, Head_Dim=128, Bytes_Per_Element=2 (FP16) 或 1 (FP8)

## Corrected Claim

Qwen3-27B 的 KV Cache 每 token 显存占用公式：KV_Cache_per_token = 2 * Num_Layers * Num_KV_Heads * Head_Dim * Bytes_Per_Element，其中 Num_Layers=64, Num_KV_Heads=8, Head_Dim=128, Bytes_Per_Element=2 (FP16) 或 1 (FP8)

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合Transformer KV Cache计算原理（Key和Value各一份，故系数为2），Qwen3-27B的架构参数（64层、GQA 8头、128维）与公开技术报告一致，量级合理。
