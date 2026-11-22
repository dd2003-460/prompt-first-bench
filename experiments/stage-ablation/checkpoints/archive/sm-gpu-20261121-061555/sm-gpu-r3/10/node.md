# N37: AMD Radeon RX 7900 XTX 在 LLM 推理中的实际表现：显存 24GB GDDR6, 带宽 960 GB/s。由于缺乏对 FP8/INT4 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD Radeon RX 7900 XTX 在 LLM 推理中的实际表现：显存 24GB GDDR6, 带宽 960 GB/s。由于缺乏对 FP8/INT4 的硬件级加速支持（主要依赖 ROCm 软件模拟或 W4A16 路径），其推理吞吐量通常比同显存带宽的 NVIDIA 卡低 15-25% [待核验]。

## Corrected Claim

AMD Radeon RX 7900 XTX 在 LLM 推理中的实际表现：显存 24GB GDDR6, 带宽 960 GB/s。由于缺乏对 FP8/INT4 的硬件级加速支持（主要依赖 ROCm 软件模拟或 W4A16 路径），其推理吞吐量通常比同显存带宽的 NVIDIA 卡低 15-25% [待核验]。

## Evidence

检索失败: no sources from any channel (all 5 failed)
