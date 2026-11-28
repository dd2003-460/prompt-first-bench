# N7: Qwen3-27B NVFP4 量化后权重体积约为 13.5GB，在 4x V100 (总 64GB) 上 TP=4 分布下，单卡权重占用约 3.375GB，剩

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B NVFP4 量化后权重体积约为 13.5GB，在 4x V100 (总 64GB) 上 TP=4 分布下，单卡权重占用约 3.375GB，剩余可用显存为 16GB - 3.375GB - 激活/临时缓冲(约 1.5GB) ≈ 11.1GB/卡

## Corrected Claim

Qwen3-27B NVFP4 量化后权重体积约为 13.5GB，在 4x V100 (总 64GB) 上 TP=4 分布下，单卡权重占用约 3.375GB，剩余可用显存为 16GB - 3.375GB - 激活/临时缓冲(约 1.5GB) ≈ 11.1GB/卡

## Evidence

先验知识/题面给定，逻辑校验通过：NVFP4 (4-bit) 量化下 27B 参数权重体积约为 27e9 * 0.5 bytes = 13.5GB，TP=4 分片后单卡权重 3.375GB，V100 16GB 显存扣除权重及约 1.5GB 激活/缓冲后剩余约 11.1GB，数值量级与算术逻辑均自洽。

## Search Query

Qwen3-27B NVFP4 weight size GB
