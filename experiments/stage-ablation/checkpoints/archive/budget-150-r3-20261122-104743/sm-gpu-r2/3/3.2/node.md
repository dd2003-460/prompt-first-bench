# N16: 带宽瓶颈分析 (Bandwidth Bottleneck)：在 Decode 阶段，每生成一个 token 需读取全部模型权重和 KV Cache，理论最大吞吐

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

带宽瓶颈分析 (Bandwidth Bottleneck)：在 Decode 阶段，每生成一个 token 需读取全部模型权重和 KV Cache，理论最大吞吐量 ≈ GPU_Memory_Bandwidth / (Weight_Memory + KV_Memory)，需对比各硬件带宽与 N7/N8 计算的显存占用

## Corrected Claim

带宽瓶颈分析 (Bandwidth Bottleneck)：在 Decode 阶段，每生成一个 token 需读取全部模型权重和 KV Cache，理论最大吞吐量 ≈ GPU_Memory_Bandwidth / (Weight_Memory + KV_Memory)，需对比各硬件带宽与 N7/N8 计算的显存占用

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段为内存带宽受限（Memory-Bound），吞吐量受限于每token需读取的总数据量（权重+KV Cache）与显存带宽之比，公式推导符合基本物理/工程直觉。
