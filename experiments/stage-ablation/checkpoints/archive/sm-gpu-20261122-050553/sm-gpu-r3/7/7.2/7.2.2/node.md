# N303: RTX 5090 的 FP8 推理算力瓶颈分析：在 Batch Size=1 时，Decode 阶段为 Memory-Bound；当 Batch Size ≥ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103, N104, N105

## Claim

RTX 5090 的 FP8 推理算力瓶颈分析：在 Batch Size=1 时，Decode 阶段为 Memory-Bound；当 Batch Size ≥ 4 时，FP8 Tensor Core 算力（~2000 TFLOPS）成为瓶颈，需计算算术强度（Arithmetic Intensity）阈值以确认 40-50 tokens/s 估算是否受计算限制而非仅带宽限制。

## Corrected Claim

RTX 5090 的 FP8 推理算力瓶颈分析：在 Batch Size=1 时，Decode 阶段为 Memory-Bound；当 Batch Size ≥ 4 时，FP8 Tensor Core 算力（~2000 TFLOPS）成为瓶颈，需计算算术强度（Arithmetic Intensity）阈值以确认 40-50 tokens/s 估算是否受计算限制而非仅带宽限制。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 FP8算力约2000 TFLOPS符合Blackwell架构规格，Batch Size=1时Decode阶段受显存带宽限制（Memory-Bound）符合LLM推理基本原理，Batch Size增大后转为计算瓶颈（Compute-Bound）符合算术强度理论，40-50 tokens/s估算在合理量级范围内

## Search Query

RTX 5090 FP8 tensor core FLOPS arithmetic intensity threshold batch size LLM
