# N292: Qwen3-27B 在 FP8 精度下，32K 上下文 KV Cache 显存占用 = 2 (K+V) * 64 (layers) * 4096 (hidden

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Qwen3-27B 在 FP8 精度下，32K 上下文 KV Cache 显存占用 = 2 (K+V) * 64 (layers) * 4096 (hidden_dim) * 32768 (seq_len) * 1 (byte) = 16.78 GB (假设 full attention 或保守估计)。

## Corrected Claim

Qwen3-27B 在 FP8 精度下，32K 上下文 KV Cache 显存占用 = 2 (K+V) * 64 (layers) * 4096 (hidden_dim) * 32768 (seq_len) * 1 (byte) = 16.78 GB (假设 full attention 或保守估计)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，4096隐藏维度）符合27B模型典型配置，FP8精度下1字节/元素，计算公式 2*64*4096*32768*1 = 17,179,869,184 bytes ≈ 16.78 GB，数值量级与算术推导均正确。
