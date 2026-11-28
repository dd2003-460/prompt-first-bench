# N23: 4×V100-16GB 运行 Qwen3.8-27B (NVFP4, TP=4) 的理论峰值吞吐量上限约为 200-300 tokens/s (聚合)，基于 H

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

4×V100-16GB 运行 Qwen3.8-27B (NVFP4, TP=4) 的理论峰值吞吐量上限约为 200-300 tokens/s (聚合)，基于 HBM2 带宽 900GB/s × 4 卡及 FP4 权重大小 13.5GB 计算的带宽瓶颈估算值 [待核验]

## Corrected Claim

4×V100-16GB 运行 Qwen3.8-27B (NVFP4, TP=4) 的理论带宽瓶颈估算吞吐量约为 200-300 tokens/s (聚合)，基于假设的 HBM2 总带宽 3.6TB/s 及 FP4 权重大小约 13.5GB 计算得出，实际性能受计算和通信开销限制可能更低。

## Evidence

[质询]该陈述包含具体的硬件参数（HBM2带宽900GB/s）和模型量化后大小（13.5GB），属于经验事实。虽然逻辑推导（带宽/权重大小）在理想情况下成立，但缺乏来源支持具体数值，且实际吞吐量受计算瓶颈、通信开销等影响，通常低于纯带宽理论上限。 | 经验事实，逻辑自洽但缺来源支持。根据带宽瓶颈估算公式 Throughput ≈ Bandwidth / Weight_Size，900GB/s * 4 / 13.5GB ≈ 266 tokens/s，落在200-300区间内，逻辑合理。但因无外部来源验证具体硬件参数和模型大小，且为经验事实，降级处理。

## Search Query

V100 16GB HBM2 bandwidth 900GB/s theoretical throughput large language model inference
