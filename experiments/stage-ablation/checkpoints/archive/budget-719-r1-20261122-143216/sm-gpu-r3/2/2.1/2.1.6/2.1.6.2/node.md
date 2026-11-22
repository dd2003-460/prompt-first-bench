# N203: RTX 3090 显存带宽为 936 GB/s，在 Qwen3-27B FP8 精度（权重 27GB）下，单卡 Decode 理论吞吐量上限计算公式为 936 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

RTX 3090 显存带宽为 936 GB/s，在 Qwen3-27B FP8 精度（权重 27GB）下，单卡 Decode 理论吞吐量上限计算公式为 936 GB/s / 27 GB × 0.85 (带宽利用率) ≈ 29.5 tokens/s，满足最低可用性阈值（>10 tokens/s）

## Corrected Claim

RTX 3090 显存带宽为 936 GB/s，在 Qwen3-27B FP8 精度（权重 27GB）下，单卡 Decode 理论吞吐量上限计算公式为 936 GB/s / 27 GB × 0.85 (带宽利用率) ≈ 29.5 tokens/s，满足最低可用性阈值（>10 tokens/s）

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 显存带宽 936 GB/s 为准确规格；Qwen3-27B FP8 权重约 27GB 符合参数量与精度估算；Decode 阶段为内存带宽瓶颈，理论吞吐量 = 带宽 / 权重大小 × 利用率，计算 936/27*0.85 ≈ 29.5 tokens/s 逻辑自洽且量级合理。
