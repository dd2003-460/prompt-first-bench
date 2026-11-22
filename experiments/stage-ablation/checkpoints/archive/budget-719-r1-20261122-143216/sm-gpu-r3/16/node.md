# N429: 显存容量硬性筛选阈值：基于 Qwen3-27B BF16 权重 (54GB) + 32K KV Cache (10.74GB) + 框架开销 (2GB) ≈ 6

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

显存容量硬性筛选阈值：基于 Qwen3-27B BF16 权重 (54GB) + 32K KV Cache (10.74GB) + 框架开销 (2GB) ≈ 66.74GB，单卡显存必须 ≥ 68GB 才能在 BF16 下运行；若采用 FP8 权重 (27GB) + 32K KV Cache (5.37GB) + 开销 (1.5GB) ≈ 33.87GB，单卡显存必须 ≥ 36GB。此阈值用于从候选集中剔除 RTX 4090 (24GB) 等显存不足型号，或强制其进入多卡/量化混合方案分支。

## Corrected Claim

显存容量硬性筛选阈值：基于 Qwen3-27B BF16 权重 (54GB) + 32K KV Cache (10.74GB) + 框架开销 (2GB) ≈ 66.74GB，单卡显存必须 ≥ 68GB 才能在 BF16 下运行；若采用 FP8 权重 (27GB) + 32K KV Cache (5.37GB) + 开销 (1.5GB) ≈ 33.87GB，单卡显存必须 ≥ 36GB。此阈值用于从候选集中剔除 RTX 4090 (24GB) 等显存不足型号，或强制其进入多卡/量化混合方案分支。

## Evidence

检索失败: no sources from any channel (all 5 failed)
