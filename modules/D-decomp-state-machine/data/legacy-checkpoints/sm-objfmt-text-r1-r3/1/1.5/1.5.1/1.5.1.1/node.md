# N118: 修正 N51/N73 矛盾：RTX 4090 BF16 峰值算力确认为 82.6 TFLOPS（非 N73 误标的 165），FP8 峰值为 165.2 TFL

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

修正 N51/N73 矛盾：RTX 4090 BF16 峰值算力确认为 82.6 TFLOPS（非 N73 误标的 165），FP8 峰值为 165.2 TFLOPS；在 Decode 阶段 (Batch=1)，瓶颈为显存带宽而非算力，因此算力数值不影响 N37 的带宽下限结论，但影响 Prefill 效率计算。

## Corrected Claim

修正 N51/N73 矛盾：RTX 4090 BF16 峰值算力确认为 82.6 TFLOPS（非 N73 误标的 165），FP8 峰值为 165.2 TFLOPS；在 Decode 阶段 (Batch=1)，瓶颈为显存带宽而非算力，因此算力数值不影响 N37 的带宽下限结论，但影响 Prefill 效率计算。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 FP8 峰值约 165 TFLOPS，BF16 为其一半约 82.5 TFLOPS，数值量级准确；Decode 阶段 Batch=1 受显存带宽限制而非算力限制，符合大模型推理基本原理。
