# N425: 显存容量档位筛选阈值：基于 Qwen3-27B 在 W4/NVFP4 精度下的最小显存需求 21.0 GB (13.5GB 权重 + 3.98GB KV + 2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

显存容量档位筛选阈值：基于 Qwen3-27B 在 W4/NVFP4 精度下的最小显存需求 21.0 GB (13.5GB 权重 + 3.98GB KV + 2.5GB Act + 1.0GB Overhead)，候选硬件单卡显存必须 ≥ 24GB。因此，16GB 显存卡（如 RTX 4060 Ti 16GB, RX 7800 XT 16GB）即使带宽足够也因容量不足被硬性排除；24GB 卡（RTX 4090, RX 7900 XTX）和 32GB+ 卡（RTX 5090, H100）为有效候选。

## Corrected Claim

显存容量档位筛选阈值：基于 Qwen3-27B 在 W4/NVFP4 精度下的最小显存需求 21.0 GB (13.5GB 权重 + 3.98GB KV + 2.5GB Act + 1.0GB Overhead)，候选硬件单卡显存必须 ≥ 24GB。因此，16GB 显存卡（如 RTX 4060 Ti 16GB, RX 7800 XT 16GB）即使带宽足够也因容量不足被硬性排除；24GB 卡（RTX 4090, RX 7900 XTX）和 32GB+ 卡（RTX 5090, H100）为有效候选。

## Evidence

检索失败: no sources from any channel (all 5 failed)
