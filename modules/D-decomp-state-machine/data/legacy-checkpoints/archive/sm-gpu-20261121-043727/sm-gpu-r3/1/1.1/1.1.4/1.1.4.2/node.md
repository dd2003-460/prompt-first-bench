# N113: 基于修正后的 GQA 参数 (num_kv_heads=4) 重新计算 32K 上下文下的单批次 KV Cache 显存占用：KV_GB = 2 (K+V) *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

基于修正后的 GQA 参数 (num_kv_heads=4) 重新计算 32K 上下文下的单批次 KV Cache 显存占用：KV_GB = 2 (K+V) * 64 (layers) * 4 (kv_heads) * 128 (head_dim) * 32768 (seq_len) * 2 (bytes) / 1024^3 ≈ 4.0 GB，此数值取代 N43 中基于 num_kv_heads=8 估算的 8.0 GB，直接决定剩余显存用于 Activation 和 Batch 的额度

## Corrected Claim

基于修正后的 GQA 参数 (num_kv_heads=4) 重新计算 32K 上下文下的单批次 KV Cache 显存占用：KV_GB = 2 (K+V) * 64 (layers) * 4 (kv_heads) * 128 (head_dim) * 32768 (seq_len) * 2 (bytes) / 1024^3 ≈ 4.0 GB，此数值取代 N43 中基于 num_kv_heads=8 估算的 8.0 GB，直接决定剩余显存用于 Activation 和 Batch 的额度

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2*64*4*128*32768*2 / 1024^3 = 4.0 GB 准确无误，且符合 GQA 显存占用线性缩放规律（8 heads -> 4 heads, 8GB -> 4GB）。
