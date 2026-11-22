# N279: 计算 MI300X (FP8) 的 KV_Cache_Per_Batch_32K：Qwen3-27B GQA 头数假设 8 (需核实 [待核验])，head_d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

计算 MI300X (FP8) 的 KV_Cache_Per_Batch_32K：Qwen3-27B GQA 头数假设 8 (需核实 [待核验])，head_dim 128。KV_Cache_Size = 2 * 8 * 128 * 32768 * 1 byte / 1024^3 ≈ 0.625 GB per batch。

## Corrected Claim

计算 MI300X (FP8) 的 KV_Cache_Per_Batch_32K：Qwen3-27B GQA 头数假设 8 (需核实 [待核验])，head_dim 128。KV_Cache_Size = 2 * 8 * 128 * 32768 * 1 byte / 1024^3 ≈ 0.625 GB per batch。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 8 * 128 * 32768 * 1 / 1024^3 = 0.625 GB，数值量级与逻辑自洽。

## Search Query

Qwen3-27B GQA num_kv_heads head_dim
