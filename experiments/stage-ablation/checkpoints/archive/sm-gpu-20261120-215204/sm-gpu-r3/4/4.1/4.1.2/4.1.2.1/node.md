# N276: 单请求 (Batch=1) 32K 序列的激活值峰值显存估算：对于 Qwen3-27B (HiddenDim=4096, IntermediateDim=110

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97

## Claim

单请求 (Batch=1) 32K 序列的激活值峰值显存估算：对于 Qwen3-27B (HiddenDim=4096, IntermediateDim=11008)，在 FlashAttention-2 优化下，激活值主要受 FFN 中间层影响，峰值约为 2 * 32768 * 11008 * 2 bytes (BF16) ≈ 1.44 GB；若未启用 FlashAttention 或保留完整 Attention 矩阵，峰值可能高达 10GB+。

## Corrected Claim

单请求 (Batch=1) 32K 序列的激活值峰值显存估算：对于 Qwen3-27B (HiddenDim=4096, IntermediateDim=11008)，在 FlashAttention-2 优化下，激活值主要受 FFN 中间层影响，峰值约为 2 * 32768 * 11008 * 2 bytes (BF16) ≈ 1.44 GB；若未启用 FlashAttention 或保留完整 Attention 矩阵，峰值可能高达 10GB+。

## Evidence

先验知识/题面给定，逻辑校验通过：FFN中间层激活值计算 2 * 32768 * 11008 * 2 bytes ≈ 1.44 GB 符合数学推导，FlashAttention下注意力矩阵不驻留显存的特性符合技术原理。
