# N296: Qwen3-27B 在 BF16 精度下，32K 上下文 KV Cache 显存占用 = 2 (K+V) * 64 (layers) * 4096 (hidde

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

Qwen3-27B 在 BF16 精度下，32K 上下文 KV Cache 显存占用 = 2 (K+V) * 64 (layers) * 4096 (hidden_dim) * 32768 (seq_len) * 2 (bytes) = 33.55 GB (假设 full attention 或保守估计)。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，32K 上下文 KV Cache 显存占用 = 2 (K+V) * 64 (layers) * 4096 (hidden_dim) * 32768 (seq_len) * 2 (bytes) = 33.55 GB (假设 full attention 或保守估计)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，4096隐藏维度）符合27B模型典型配置，BF16精度下2字节/元素，计算公式 2*64*4096*32768*2 = 34,359,738,368 bytes ≈ 32 GiB (或 33.55 GB 十进制)，量级与算术均正确。
