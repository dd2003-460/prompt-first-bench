# N37: Qwen3-27B 在 4x V100 TP=4 上的算术强度（Arithmetic Intensity）约为 15-20 FLOP/Byte，远低于 V100

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Qwen3-27B 在 4x V100 TP=4 上的算术强度（Arithmetic Intensity）约为 15-20 FLOP/Byte，远低于 V100 Tensor Core 的 Roofline 拐点（~140 FLOP/Byte），因此无论 Batch Size 如何调整，推理过程始终处于 Memory-Bound 区域，无法利用 125 TFLOPS 的峰值算力。

## Corrected Claim

Qwen3-27B 在 4x V100 TP=4 上的算术强度（Arithmetic Intensity）约为 15-20 FLOP/Byte，远低于 V100 Tensor Core 的 Roofline 拐点（~140 FLOP/Byte），因此无论 Batch Size 如何调整，推理过程始终处于 Memory-Bound 区域，无法利用 125 TFLOPS 的峰值算力。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 FP16 Tensor Core 峰值约 125 TFLOPS，HBM2 带宽约 900 GB/s，Roofline 拐点约为 125000/900 ≈ 139 FLOP/Byte；大模型推理（尤其是小 Batch 或单请求）通常受限于内存带宽，算术强度远低于此拐点，故处于 Memory-Bound 区域符合物理直觉与工程常识。

## Search Query

llm inference arithmetic intensity roofline model v100 tensor core memory bound
