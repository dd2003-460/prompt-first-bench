# N92: 单卡高性低成工作点：RTX 4090 24GB 运行 Qwen3-27B W4A16 (13.5GB 权重 + ~5.7GB 其他 ≈ 19.2GB < 24G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28, N29, N30

## Claim

单卡高性低成工作点：RTX 4090 24GB 运行 Qwen3-27B W4A16 (13.5GB 权重 + ~5.7GB 其他 ≈ 19.2GB < 24GB)，理论吞吐下限 ≈ 13.5GB / 1008GB/s ≈ 13.4ms/token (≈74 tok/s)，实际吞吐预计 40-50 tok/s，TCO_5yr ≈ $1599 + 5 * (650W * 8h * 365d * $0.15) ≈ $1599 + $1423 ≈ $3022

## Corrected Claim

单卡高性低成工作点：RTX 4090 24GB 运行 Qwen3-27B W4A16 (13.5GB 权重 + ~5.7GB 其他 ≈ 19.2GB < 24GB)，理论吞吐下限 ≈ 13.5GB / 1008GB/s ≈ 13.4ms/token (≈74 tok/s)，实际吞吐预计 40-50 tok/s，TCO_5yr ≈ $1599 + 5 * (650W * 8h * 365d * $0.15) ≈ $1599 + $1423 ≈ $3022

## Evidence

先验知识/题面给定，逻辑校验通过：显存占用（13.5+5.7=19.2GB < 24GB）合理；带宽瓶颈计算（13.5GB/1008GB/s≈13.4ms）符合物理直觉；TCO计算（硬件+电费）数值量级正确。
