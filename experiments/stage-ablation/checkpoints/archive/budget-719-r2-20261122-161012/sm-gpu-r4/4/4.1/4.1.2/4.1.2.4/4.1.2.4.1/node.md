# N494: 64K 上下文下 KV Cache 的精确计算修正：Qwen3-27B 有 40 层，每层 GQA 头数 32（KV 头 8），Head Dim 128。单 T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N203

## Claim

64K 上下文下 KV Cache 的精确计算修正：Qwen3-27B 有 40 层，每层 GQA 头数 32（KV 头 8），Head Dim 128。单 Token KV 大小 = 2 (K+V) * 40 (Layers) * 8 (KV Heads) * 128 (Dim) * 2 (Bytes/BF16) = 163,840 Bytes ≈ 160 KB/Token。64K 上下文单请求 KV 占用 = 65536 * 160 KB ≈ 10.24 GB，而非 N203 所述的 16GB（N203 可能误用了 MHA 或计算错误）。

## Corrected Claim

64K 上下文下 KV Cache 的精确计算修正：Qwen3-27B 有 40 层，每层 GQA 头数 32（KV 头 8），Head Dim 128。单 Token KV 大小 = 2 (K+V) * 40 (Layers) * 8 (KV Heads) * 128 (Dim) * 2 (Bytes/BF16) = 163,840 Bytes ≈ 160 KB/Token。64K 上下文单请求 KV 占用 = 65536 * 160 KB ≈ 10.24 GB，而非 N203 所述的 16GB（N203 可能误用了 MHA 或计算错误）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Qwen3-27B的GQA架构参数（40层，8 KV头，128维，BF16），单Token KV缓存计算为 2*40*8*128*2 = 163,840 Bytes (160 KB)，64K上下文总占用 65536 * 160 KB = 10.24 GB，数学推导正确且量级合理。
