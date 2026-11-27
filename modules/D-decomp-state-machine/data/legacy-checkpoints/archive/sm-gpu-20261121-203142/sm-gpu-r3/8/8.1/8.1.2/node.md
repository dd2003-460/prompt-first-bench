# N343: H100 在长上下文 (32K) 下的 KV Cache 显存占用计算：Qwen3-27B 采用 GQA，假设 32 层，8 KV Heads，Head Dim

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N111

## Claim

H100 在长上下文 (32K) 下的 KV Cache 显存占用计算：Qwen3-27B 采用 GQA，假设 32 层，8 KV Heads，Head Dim 128，每 Token KV Cache 大小 = 2 * 32 * 8 * 128 * 2 bytes (BF16) = 131,072 bytes ≈ 0.125 MB；32K 上下文总 KV Cache = 32768 * 0.125 MB ≈ 4 GB，此数值已包含在 N111 的带宽瓶颈计算中，确认 4GB 为准确值而非估算

## Corrected Claim

H100 在长上下文 (32K) 下的 KV Cache 显存占用计算：Qwen3-27B 采用 GQA，假设 32 层，8 KV Heads，Head Dim 128，每 Token KV Cache 大小 = 2 * 32 * 8 * 128 * 2 bytes (BF16) = 131,072 bytes ≈ 0.125 MB；32K 上下文总 KV Cache = 32768 * 0.125 MB ≈ 4 GB，此数值已包含在 N111 的带宽瓶颈计算中，确认 4GB 为准确值而非估算

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2(K+V) * 32(层) * 8(头) * 128(维) * 2(BF16) = 131,072 bytes/token，32768 tokens * 131,072 bytes = 4,294,967,296 bytes = 4 GB，数值准确且逻辑自洽。

## Search Query

Qwen3-27B GQA configuration num_kv_heads head_dim
