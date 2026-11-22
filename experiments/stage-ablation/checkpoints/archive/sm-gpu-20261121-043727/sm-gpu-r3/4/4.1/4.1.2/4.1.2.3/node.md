# N164: 基于 N112 和 N113 的 KV Cache 值，计算在 RTX 4090 (24GB) 和 H100 (80GB) 上，扣除权重 (BF16: 54GB

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

基于 N112 和 N113 的 KV Cache 值，计算在 RTX 4090 (24GB) 和 H100 (80GB) 上，扣除权重 (BF16: 54GB, FP8: 27GB) 和系统开销 (2GB) 后，可支持的最大并发 Batch Size：Batch_Size = (VRAM_Total - Weight_Size - System_Overhead) / KV_Cache_Per_Batch。例如，RTX 4090 FP8: (24 - 27 - 2) < 0，不可行；H100 FP8: (80 - 27 - 2) / 3.75 ≈ 13 并发。

## Corrected Claim

基于 N112 和 N113 的 KV Cache 值，计算在 RTX 4090 (24GB) 和 H100 (80GB) 上，扣除权重 (BF16: 54GB, FP8: 27GB) 和系统开销 (2GB) 后，可支持的最大并发 Batch Size：Batch_Size = (VRAM_Total - Weight_Size - System_Overhead) / KV_Cache_Per_Batch。例如，RTX 4090 FP8: (24 - 27 - 2) < 0，不可行；H100 FP8: (80 - 27 - 2) / 3.75 ≈ 13 并发。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 (80-27-2)/3.75 = 51/3.75 = 13.6，向下取整为13，符合显存分配逻辑；RTX 4090 显存不足导致不可行的判断也符合逻辑。
