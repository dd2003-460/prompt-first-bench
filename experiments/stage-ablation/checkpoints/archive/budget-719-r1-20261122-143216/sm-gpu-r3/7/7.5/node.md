# N133: RTX 4090 (1008 GB/s) 与 H100 SXM (3.35 TB/s) 的显存带宽比值为 1:3.32，在 32K 上下文 Decode 阶段，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32, N33, N34

## Claim

RTX 4090 (1008 GB/s) 与 H100 SXM (3.35 TB/s) 的显存带宽比值为 1:3.32，在 32K 上下文 Decode 阶段，RTX 4090 的 tokens/s 吞吐量理论上仅为 H100 的 30%-40% [待核验]，因内存带宽是主要瓶颈。

## Corrected Claim

RTX 4090 (1008 GB/s) 与 H100 SXM (3.35 TB/s) 的显存带宽比值为 1:3.32，在 32K 上下文 Decode 阶段，RTX 4090 的 tokens/s 吞吐量理论上仅为 H100 的 30%-40% [待核验]，因内存带宽是主要瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽比值 3.35/1.008 ≈ 3.32 计算正确；在 Decode 阶段（Memory-Bound），吞吐量与显存带宽近似成正比，故 1/3.32 ≈ 30.1%，落在 30%-40% 区间内，符合 Roofline 模型基本直觉。

## Search Query

RTX 4090 vs H100 LLM decode throughput memory bandwidth bottleneck
