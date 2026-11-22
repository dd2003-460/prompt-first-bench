# N336: 单请求 32K 上下文下的 KV Cache 显存占用 (VRAM_per_request_32K) 在 FP8 精度下为 5.37 GB，在 BF16 精度下

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

单请求 32K 上下文下的 KV Cache 显存占用 (VRAM_per_request_32K) 在 FP8 精度下为 5.37 GB，在 BF16 精度下为 10.74 GB，该值由 N107 和 N109 中的公式计算得出，且假设 KV Cache 采用 FP8/BF16 存储

## Corrected Claim

单请求 32K 上下文下的 KV Cache 显存占用 (VRAM_per_request_32K) 在 FP8 精度下为 5.37 GB，在 BF16 精度下为 10.74 GB，该值由 N107 和 N109 中的公式计算得出，且假设 KV Cache 采用 FP8/BF16 存储

## Evidence

先验知识/题面给定，逻辑校验通过：BF16 是 FP8 的 2 倍精度，10.74 GB 恰好是 5.37 GB 的 2 倍，数值关系自洽且符合 KV Cache 显存占用与精度线性相关的物理直觉。
