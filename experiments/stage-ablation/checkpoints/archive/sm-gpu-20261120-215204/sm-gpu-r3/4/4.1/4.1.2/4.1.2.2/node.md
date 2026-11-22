# N277: KV Cache 显存占用的精确计算修正：Qwen3-27B 采用 GQA (8 KV Heads, HeadDim 128)，每 Token KV Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97

## Claim

KV Cache 显存占用的精确计算修正：Qwen3-27B 采用 GQA (8 KV Heads, HeadDim 128)，每 Token KV Cache 大小 = 2 (K+V) * 64 (Layers) * 8 (Heads) * 128 (Dim) * 2 (Bytes) = 262,144 bytes ≈ 0.25 MB/Token。32K 上下文下，KV Cache 总占用 = 32768 * 0.25 MB ≈ 8 GB (而非 N97 中估算的 40GB，后者可能误用了 MHA 或 BF16 全精度非 GQA 假设)。

## Corrected Claim

KV Cache 显存占用的精确计算修正：Qwen3-27B 采用 GQA (8 KV Heads, HeadDim 128)，每 Token KV Cache 大小 = 2 (K+V) * 64 (Layers) * 8 (Heads) * 128 (Dim) * 2 (Bytes) = 262,144 bytes ≈ 0.25 MB/Token。32K 上下文下，KV Cache 总占用 = 32768 * 0.25 MB ≈ 8 GB (而非 N97 中估算的 40GB，后者可能误用了 MHA 或 BF16 全精度非 GQA 假设)。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2*64*8*128*2 = 262,144 bytes = 0.25 MB/Token 准确，32K 上下文总占用 8GB 符合 GQA 架构下的显存估算逻辑。
