# N382: Qwen3-27B 在 Decode 阶段（Batch=1）的算术强度（Arithmetic Intensity）约为 1-2 FLOPs/Byte，远低于 R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N134

## Claim

Qwen3-27B 在 Decode 阶段（Batch=1）的算术强度（Arithmetic Intensity）约为 1-2 FLOPs/Byte，远低于 RTX 5090 的平衡点（~58 FLOPs/Byte）和 H100 的平衡点（~295 FLOPs/Byte），因此两者均处于完全内存带宽受限区域，理论吞吐量比值应趋近于带宽比值 1:1.87 的倒数（即 5090 约为 H100 的 53.5%）。

## Corrected Claim

Qwen3-27B 在 Decode 阶段（Batch=1）的算术强度（Arithmetic Intensity）约为 1-2 FLOPs/Byte，远低于 RTX 5090 的平衡点（~58 FLOPs/Byte）和 H100 的平衡点（~295 FLOPs/Byte），因此两者均处于完全内存带宽受限区域，理论吞吐量比值应趋近于带宽比值 1:1.87 的倒数（即 5090 约为 H100 的 53.5%）。

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段Batch=1时算术强度确实极低（~1-2 FLOPs/Byte），远低于GPU平衡点，处于内存带宽受限区，吞吐量比值趋近于带宽比值的倒数（1/1.87 ≈ 53.5%），逻辑自洽且数值量级合理。

## Search Query

Roofline model arithmetic intensity LLM decode batch 1 memory bound
