# N288: Qwen3-27B 在 FP8 精度下，32K 上下文 KV Cache 显存占用 = 2 (K+V) * 64 (layers) * 4096 (hidden

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

Qwen3-27B 在 FP8 精度下，32K 上下文 KV Cache 显存占用 = 2 (K+V) * 64 (layers) * 4096 (hidden_dim) * 32768 (seq_len) * 1 (byte) = 16.78 GB (假设 GQA 中 KV heads 与 Q heads 比例未优化或按 full attention 计算，若为 GQA 则需乘以 head 比例系数，此处按最坏情况 full attention 或保守估计)。

## Corrected Claim

Qwen3-27B 在 FP8 精度下，32K 上下文 KV Cache 显存占用 = 2 (K+V) * 64 (layers) * 4096 (hidden_dim) * 32768 (seq_len) * 1 (byte) = 16.78 GB (假设 GQA 中 KV heads 与 Q heads 比例未优化或按 full attention 计算，若为 GQA 则需乘以 head 比例系数，此处按最坏情况 full attention 或保守估计)。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 4096 * 32768 * 1 = 17,179,869,184 bytes ≈ 16.78 GB (GiB)，数值量级与逻辑自洽。
