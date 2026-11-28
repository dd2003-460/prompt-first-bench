# N43: MTP 验证阶段的计算复杂度与 Draft 长度成正比，V100 单卡有效 FP16 算力约为 15.7 TFLOPS，相比 A100 (312 TFLOPS)

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

MTP 验证阶段的计算复杂度与 Draft 长度成正比，V100 单卡有效 FP16 算力约为 15.7 TFLOPS，相比 A100 (312 TFLOPS) 低约 20 倍，导致在同等 Batch Size 下，Target Model 验证 4 个 Draft Token 的延迟约为 A100 的 15-20 倍。

## Corrected Claim

MTP 验证阶段的计算复杂度与 Draft 长度成正比，V100 单卡有效 FP16 算力远低于 A100 (312 TFLOPS)，导致在同等 Batch Size 下，Target Model 验证 4 个 Draft Token 的延迟显著高于 A100。

## Evidence

[质询]V100 单卡有效 FP16 算力约为 15.7 TFLOPS 这一数值严重偏离常识，V100 的 FP16 峰值算力通常在 125-130 TFLOPS 左右，即便考虑极低利用率，15.7 TFLOPS 也显得过低，可能导致倍数估算失真。 | 先验知识/题面给定，逻辑校验通过，但 V100 算力数值存疑，故降级。
