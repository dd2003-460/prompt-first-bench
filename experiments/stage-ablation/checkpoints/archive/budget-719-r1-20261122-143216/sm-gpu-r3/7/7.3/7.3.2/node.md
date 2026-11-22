# N371: L40S 在 FP8 精度下的理论 FP8 Tensor Core 峰值算力为 362 TFLOPS，而 RTX 5090 为 1050 TFLOPS (FP1

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N131

## Claim

L40S 在 FP8 精度下的理论 FP8 Tensor Core 峰值算力为 362 TFLOPS，而 RTX 5090 为 1050 TFLOPS (FP16) / ~525 TFLOPS (FP8 估计)，L40S 的算力/带宽比 (Arithmetic Intensity) 较低，在 Batch=1 时完全受带宽限制，但在 Batch>4 时可能受算力限制，需计算 Break-even Batch Size 以确定其性能拐点。

## Corrected Claim

L40S 在 FP8 精度下的理论峰值算力约为 362 TFLOPS，RTX 5090 的 FP16 峰值算力约为 1050 TFLOPS（FP8 算力约为其两倍，即 ~2100 TFLOPS，若按标准 FP8=2x FP16 换算；若原陈述中 ~525 TFLOPS 为特定稀疏或低精度模式下的估计，则需注明口径）。L40S 的算力/带宽比相对较低，在 Batch=1 时受带宽限制，Batch 增大后逐渐转向算力限制，具体 Break-even Batch Size 需根据具体模型结构和硬件带宽精确计算。

## Evidence

[质询]RTX 5090 的 FP8 算力估计值（~525 TFLOPS）存在显著不确定性，且 L40S 的 FP8 峰值算力（362 TFLOPS）与常见公开数据（通常引用为 362 TFLOPS FP8 或 733 TFLOPS FP8 取决于是否包含稀疏性/具体架构定义）可能存在口径混淆；此外，Break-even Batch Size 的具体数值未给出，仅定性描述，缺乏精确量化支持。 | 先验知识/题面给定，逻辑校验通过：L40S 和 RTX 5090 的算力量级符合 NVIDIA 官方规格的大致范围（L40S FP8 约 362 TFLOPS 是常见引用值，RTX 5090 FP16 1050 TFLOPS 符合 Blackwell 架构预期），带宽限制与算力限制的转换逻辑（Arithmetic Intensity 与 Batch Size 的关系）在深度学习推理中是标准理论，逻辑自洽。但 RTX 5090 FP8 具体数值为估计值，且无外部来源直接确认 Break-even Batch Size 的具体计算结果，故降级。
