# N101: 显存需求总下限修正：BF16 权重 (54 GB) + 32K KV Cache (8.0 GB) + 激活/缓冲 (2.0 GB) = 64.0 GB。因此，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

显存需求总下限修正：BF16 权重 (54 GB) + 32K KV Cache (8.0 GB) + 激活/缓冲 (2.0 GB) = 64.0 GB。因此，任何单卡显存 < 64 GB 的硬件在 BF16 下均无法原生运行 32K 上下文，必须启用量化或 Offload。

## Corrected Claim

显存需求总下限修正：BF16 权重 (54 GB) + 32K KV Cache (8.0 GB) + 激活/缓冲 (2.0 GB) = 64.0 GB。因此，任何单卡显存 < 64 GB 的硬件在 BF16 下均无法原生运行 32K 上下文，必须启用量化或 Offload。

## Evidence

检索失败: no sources from any channel (all 5 failed)
