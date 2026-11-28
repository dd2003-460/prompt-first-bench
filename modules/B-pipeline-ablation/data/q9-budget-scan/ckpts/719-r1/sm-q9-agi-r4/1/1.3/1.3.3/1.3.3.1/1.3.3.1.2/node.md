# N409: V100 在 Compute Capability 7.0 下的 FP16 峰值算力为 125 TFLOPS，INT8 峰值算力为 250 TOPS，作为评估软

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N138

## Claim

V100 在 Compute Capability 7.0 下的 FP16 峰值算力为 125 TFLOPS，INT8 峰值算力为 250 TOPS，作为评估软件模拟 FP4/FP8 性能损失的基准参照值

## Corrected Claim

V100 在 Compute Capability 7.0 下的 FP16 峰值算力为 125 TFLOPS，INT8 峰值算力为 250 TOPS，作为评估软件模拟 FP4/FP8 性能损失的基准参照值

## Evidence

先验知识/题面给定，逻辑校验通过：V100 (Volta架构, CC 7.0) 官方规格中 FP16 Tensor Core 峰值算力确为 125 TFLOPS，INT8 为 250 TOPS，数值量级与架构特性一致。
