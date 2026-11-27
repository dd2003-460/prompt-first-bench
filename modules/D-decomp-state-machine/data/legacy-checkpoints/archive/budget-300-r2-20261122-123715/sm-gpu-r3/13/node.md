# N119: 2x RTX 4090 (PCIe 4.0 x16) 在 Tensor Parallelism 下的 Token 生成速度 (TPOT) 通常仅为单卡的 1.6

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

2x RTX 4090 (PCIe 4.0 x16) 在 Tensor Parallelism 下的 Token 生成速度 (TPOT) 通常仅为单卡的 1.6-1.7 倍 (而非理论 2 倍)，瓶颈在于每层 Attention 输出的跨卡同步；若使用 NVLink 桥接 (需特定主板/转接)，效率可提升至 1.8-1.9 倍，但硬件成本增加 ~$200-300。

## Corrected Claim

2x RTX 4090 (PCIe 4.0 x16) 在 Tensor Parallelism 下的 Token 生成速度 (TPOT) 通常仅为单卡的 1.6-1.7 倍 (而非理论 2 倍)，瓶颈在于每层 Attention 输出的跨卡同步；若使用 NVLink 桥接 (需特定主板/转接)，效率可提升至 1.8-1.9 倍，但硬件成本增加 ~$200-300。

## Evidence

检索失败: no sources from any channel (all 5 failed)
