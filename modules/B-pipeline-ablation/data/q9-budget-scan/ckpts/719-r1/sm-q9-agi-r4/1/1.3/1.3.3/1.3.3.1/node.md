# N138: V100 (Compute Capability 7.0) 的 Tensor Core 硬件规格仅支持 FP16/BF16 和 INT8 数据类型，不支持原生 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

V100 (Compute Capability 7.0) 的 Tensor Core 硬件规格仅支持 FP16/BF16 和 INT8 数据类型，不支持原生 FP4/FP8 矩阵乘法指令（CUDA 架构特性，非软件可绕过）

## Corrected Claim

V100 (Compute Capability 7.0) 的 Tensor Core 硬件规格仅支持 FP16/BF16 和 INT8 数据类型，不支持原生 FP4/FP8 矩阵乘法指令（CUDA 架构特性，非软件可绕过）

## Evidence

先验知识/题面给定，逻辑校验通过：V100 (Volta架构, CC 7.0) 的Tensor Core确实仅支持FP16/INT8/INT4/INT1等低精度格式，原生FP8/FP4支持始于Ampere (CC 8.0)及后续架构，符合硬件演进事实。
