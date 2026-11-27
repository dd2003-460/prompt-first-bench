# N787: M2 Ultra 的内存带宽为 800 GB/s，而 H100 SXM 为 3.35 TB/s。在 Prefill 阶段，若计算密度 (FLOPs/Byte) 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N245

## Claim

M2 Ultra 的内存带宽为 800 GB/s，而 H100 SXM 为 3.35 TB/s。在 Prefill 阶段，若计算密度 (FLOPs/Byte) 低于 187.5 FLOPs/Byte (Arithmetic Intensity = 148e12 / 800e9)，则受内存带宽限制。对于 27B 模型，32K 序列的 Prefill 算术强度极高，通常受算力限制，但 M2 Ultra 的算力 (148 TFLOPS) 仅为 H100 (989 TFLOPS) 的 15%，因此理论速度比约为 1:6.7，而非 1:5-10。

## Corrected Claim

M2 Ultra 的内存带宽为 800 GB/s，而 H100 SXM 为 3.35 TB/s。在 Prefill 阶段，若计算密度 (FLOPs/Byte) 低于 187.5 FLOPs/Byte (Arithmetic Intensity = 148e12 / 800e9)，则受内存带宽限制。对于 27B 模型，32K 序列的 Prefill 算术强度极高，通常受算力限制，但 M2 Ultra 的算力 (148 TFLOPS) 仅为 H100 (989 TFLOPS) 的 15%，因此理论速度比约为 1:6.7，而非 1:5-10。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra (148 TFLOPS) 与 H100 SXM (989 TFLOPS) 的算力比值约为 1:6.7，符合硬件规格事实；Prefill 阶段高算术强度受算力限制的逻辑推导自洽。

## Search Query

M2 Ultra vs H100 prefill performance benchmark LLM
