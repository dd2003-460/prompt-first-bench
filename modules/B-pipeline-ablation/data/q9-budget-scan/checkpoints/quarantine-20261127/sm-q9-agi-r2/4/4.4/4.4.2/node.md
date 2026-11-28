# N73: MacBook M1 Max (64GB) 运行 Llama-3-8B (FP16) 的推理速度预估为 15-25 tokens/s (CPU+GPU 协同)，

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

MacBook M1 Max (64GB) 运行 Llama-3-8B (FP16) 的推理速度预估为 15-25 tokens/s (CPU+GPU 协同)，显存占用 16GB，剩余 48GB 可用于其他轻量任务或作为向量数据库缓存；相比 V100 集群，其优势在于零额外电力增量成本（Mac 待机功耗极低）。

## Corrected Claim

MacBook M1 Max (64GB) 运行 Llama-3-8B (FP16) 的推理速度预估为 10-15 tokens/s（受限于统一内存带宽），显存占用约 16GB，剩余 48GB 可用于其他任务；相比 V100 集群，其优势在于无需专用服务器基础设施，但满载运行时仍有显著电力消耗。

## Evidence

[质询]数值量级与硬件架构不符：M1 Max 的 CPU 和 GPU 共享统一内存带宽（约 400GB/s），并非独立的 'CPU+GPU 协同' 双通道加速。Llama-3-8B FP16 模型大小约为 16GB，受限于内存带宽瓶颈，理论最大吞吐量约为 400GB/s / 16GB ≈ 25 tokens/s。实际推理中由于计算开销、内存访问延迟及非理想调度，速度通常显著低于理论峰值，15-25 tokens/s 的上限过于乐观，下限也偏高（通常实测在 10-15 tokens/s 左右）。此外，'零额外电力增量成本' 表述不严谨，虽然待机功耗低，但满载推理时功耗可达 60W+，并非零增量。 | 先验知识/题面给定，逻辑校验发现数值量级偏乐观且架构描述存在误导（M1 Max 为统一内存架构，非独立 CPU/GPU 带宽叠加），故降级。

## Search Query

MacBook Pro M1 Max Llama 3 8B inference speed tokens per second llama.cpp
