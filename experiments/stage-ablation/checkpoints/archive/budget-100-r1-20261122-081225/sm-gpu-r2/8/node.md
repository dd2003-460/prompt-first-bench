# N51: NVIDIA L40S 在 FP8 精度下运行 27B 模型时，由于 GDDR6 显存带宽 (864 GB/s) 远低于 HBM (2000+ GB/s)，其 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA L40S 在 FP8 精度下运行 27B 模型时，由于 GDDR6 显存带宽 (864 GB/s) 远低于 HBM (2000+ GB/s)，其 decode 阶段吞吐通常低于 RTX 4090，但 L40S 支持更大的 batch size 而不溢出显存 (48GB vs 24GB)，在高并发场景下 TCO 更优。

## Corrected Claim

NVIDIA L40S 在 FP8 精度下运行 27B 模型时，由于 GDDR6 显存带宽 (864 GB/s) 远低于 HBM (2000+ GB/s)，其 decode 阶段吞吐通常低于 RTX 4090，但 L40S 支持更大的 batch size 而不溢出显存 (48GB vs 24GB)，在高并发场景下 TCO 更优。

## Evidence

检索失败: no sources from any channel (all 5 failed)
