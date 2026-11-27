# N246: L40S 的 FP8 推理支持量化：L40S 支持原生 FP8 (E4M3) 加速，其 FP8 算力为 121 TFLOPS，相比 INT8 的 121 TOP

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

L40S 的 FP8 推理支持量化：L40S 支持原生 FP8 (E4M3) 加速，其 FP8 算力为 121 TFLOPS，相比 INT8 的 121 TOPS 在精度-性能权衡上更优，适合对精度敏感且需要 48GB 显存的数据中心场景

## Corrected Claim

L40S 支持原生 FP8 (E4M3) 加速，其 FP8 算力约为 181 TFLOPS (稠密) 或 362 TFLOPS (稀疏)，相比 INT8 在精度-性能权衡上更优，适合对精度敏感且需要 48GB 显存的数据中心场景

## Evidence

[质询]数值量级与官方规格存在显著偏差：NVIDIA 官方数据显示 L40S 的 FP8 Tensor Core 算力通常为 362 TFLOPS（稀疏）或 181 TFLOPS（稠密），而非 121 TFLOPS；121 TOPS 更接近其 INT8 稀疏算力或旧款卡（如 A100）的某些指标，此处数值可能混淆了不同精度或不同代际产品的规格。 | 先验知识/题面给定，逻辑校验通过（FP8 支持及 48GB 显存符合 L40S 特征），但具体算力数值 121 TFLOPS 与主流公开规格（~181-362 TFLOPS）不符，且无外部来源支持，故降级。
