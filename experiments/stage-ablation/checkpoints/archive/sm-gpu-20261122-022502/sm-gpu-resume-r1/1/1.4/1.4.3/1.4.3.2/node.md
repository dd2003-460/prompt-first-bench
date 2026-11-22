# N159: H100 SXM 的 HBM3 带宽为 3350 GB/s，RTX 4090 的 GDDR6X 带宽为 1008 GB/s。在 Decode 阶段（带宽受限），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

H100 SXM 的 HBM3 带宽为 3350 GB/s，RTX 4090 的 GDDR6X 带宽为 1008 GB/s。在 Decode 阶段（带宽受限），理论吞吐比 = 3350/1008 ≈ 3.32x。若考虑 N49 中提到的 1.8x-2.5x 综合优势系数，则意味着在 Prefill 阶段（计算受限）或混合负载中，H100 的相对优势被算力瓶颈部分抵消，需分别计算 Prefill FLOPs 需求与 Decode 字节需求来解构该系数。

## Corrected Claim

H100 SXM 的 HBM3 带宽为 3350 GB/s，RTX 4090 的 GDDR6X 带宽为 1008 GB/s。在 Decode 阶段（带宽受限），理论吞吐比 = 3350/1008 ≈ 3.32x。若考虑 N49 中提到的 1.8x-2.5x 综合优势系数，则意味着在 Prefill 阶段（计算受限）或混合负载中，H100 的相对优势被算力瓶颈部分抵消，需分别计算 Prefill FLOPs 需求与 Decode 字节需求来解构该系数。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM HBM3带宽(3.35TB/s)与RTX 4090 GDDR6X带宽(1TB/s)数值准确，带宽比3.32x计算正确，Decode阶段带宽受限及Prefill阶段计算受限的推理符合GPU架构基本原理。
