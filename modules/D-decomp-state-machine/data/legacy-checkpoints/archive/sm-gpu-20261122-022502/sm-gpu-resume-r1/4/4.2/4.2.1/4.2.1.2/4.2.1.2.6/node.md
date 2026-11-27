# N799: 2x RTX 4090 方案中，若采用 INT4 权重 + FP8 KV Cache，总显存占用精确重算：INT4 权重 (13.5GB) + Group-wi

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N248, N249, N250

## Claim

2x RTX 4090 方案中，若采用 INT4 权重 + FP8 KV Cache，总显存占用精确重算：INT4 权重 (13.5GB) + Group-wise 校准 (0.84GB) + FP8 KV Cache (6.59GB) + 激活值/缓冲 (2.5GB, 取 Prefill 峰值) = 23.43GB。剩余显存 = 24GB - 23.43GB = 0.57GB。结论：即使启用 PagedAttention，静态估算仍极接近 OOM 边缘，需依赖运行时动态调整 batch_size 或上下文长度。

## Corrected Claim

2x RTX 4090 方案中，若采用 INT4 权重 + FP8 KV Cache，总显存占用精确重算：INT4 权重 (13.5GB) + Group-wise 校准 (0.84GB) + FP8 KV Cache (6.59GB) + 激活值/缓冲 (2.5GB, 取 Prefill 峰值) = 23.43GB。剩余显存 = 24GB - 23.43GB = 0.57GB。结论：即使启用 PagedAttention，静态估算仍极接近 OOM 边缘，需依赖运行时动态调整 batch_size 或上下文长度。

## Evidence

先验知识/题面给定，逻辑校验通过：算术求和 13.5+0.84+6.59+2.5=23.43 正确，剩余 0.57GB 计算无误，符合显存估算逻辑。
