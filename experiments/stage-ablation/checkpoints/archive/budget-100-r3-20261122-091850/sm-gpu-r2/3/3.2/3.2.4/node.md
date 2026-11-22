# N67: Compute-Bound 与 Memory-Bound 的临界条件：当 Arithmetic Intensity (FLOPs/Byte) < GPU 的 R

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

Compute-Bound 与 Memory-Bound 的临界条件：当 Arithmetic Intensity (FLOPs/Byte) < GPU 的 Roofline 拐点 (Peak FLOPs / Peak Bandwidth) 时，性能受限于带宽；反之受限于算力。对于 RTX 4090 (82.6 TFLOPS FP16, 1008 GB/s)，拐点约为 82 FLOPs/Byte。Decode 阶段通常 FLOPs/Byte 较低，属于 Memory-Bound。

## Corrected Claim

Compute-Bound 与 Memory-Bound 的临界条件：当 Arithmetic Intensity (FLOPs/Byte) < GPU 的 Roofline 拐点 (Peak FLOPs / Peak Bandwidth) 时，性能受限于带宽；反之受限于算力。对于 RTX 4090 (82.6 TFLOPS FP16, 1008 GB/s)，拐点约为 82 FLOPs/Byte。Decode 阶段通常 FLOPs/Byte 较低，属于 Memory-Bound。

## Evidence

先验知识/题面给定，逻辑校验通过：Roofline模型定义及RTX 4090参数（82.6 TFLOPS / 1008 GB/s ≈ 82 FLOPs/Byte）符合物理直觉与工程常识，Decode阶段低算术强度属Memory-Bound为公认事实。

## Search Query

GPU roofline model arithmetic intensity decode phase memory bound
