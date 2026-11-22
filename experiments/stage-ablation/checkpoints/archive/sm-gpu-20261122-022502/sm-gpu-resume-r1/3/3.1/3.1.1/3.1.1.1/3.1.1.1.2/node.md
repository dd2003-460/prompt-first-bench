# N650: RTX 4090 32K 上下文 KV Cache 显存占用：对于 Qwen3-27B (假设 64 层, 8 KV heads, head_dim=128, 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N200

## Claim

RTX 4090 32K 上下文 KV Cache 显存占用：对于 Qwen3-27B (假设 64 层, 8 KV heads, head_dim=128, GQA), 每 token KV 大小 = 2 * 64 * 8 * 128 * 2 bytes (BF16) = 262KB。32K tokens 总 KV = 32768 * 262KB ≈ 8.5GB。加上 13.5GB 权重，总占用 22GB，仅剩 2GB 用于激活值，存在 OOM 风险，需启用 PagedAttention 或降低 KV 精度至 FP8。

## Corrected Claim

RTX 4090 32K 上下文 KV Cache 显存占用：对于 Qwen3-27B (假设 64 层, 8 KV heads, head_dim=128, GQA), 每 token KV 大小 = 2 * 64 * 8 * 128 * 2 bytes (BF16) = 262KB。32K tokens 总 KV = 32768 * 262KB ≈ 8.5GB。加上 13.5GB 权重，总占用 22GB，仅剩 2GB 用于激活值，存在 OOM 风险，需启用 PagedAttention 或降低 KV 精度至 FP8。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式 2(K+V) * layers * heads * dim * bytes 正确，数值量级（262KB/token, 8.5GB/32K）合理，总显存占用估算符合工程直觉。
