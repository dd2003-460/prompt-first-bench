# N340: A100 (Ampere) 硬件规格确认：Tensor Core 支持 FP16/BF16/INT8/INT4，但不包含 FP8 数据格式单元；其最大原生精度为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N135

## Claim

A100 (Ampere) 硬件规格确认：Tensor Core 支持 FP16/BF16/INT8/INT4，但不包含 FP8 数据格式单元；其最大原生精度为 BF16，任何 'FP8' 标签在 A100 上均指软件模拟或误标。

## Corrected Claim

A100 (Ampere) 硬件规格确认：Tensor Core 支持 FP16/BF16/INT8/INT4，但不包含 FP8 数据格式单元；其最大原生精度为 BF16，任何 'FP8' 标签在 A100 上均指软件模拟或误标。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 (Ampere架构) 确实支持 FP16/BF16/INT8/INT4 Tensor Core 运算，但不支持原生 FP8（FP8 支持始于 Hopper 架构 H100），因此 A100 上的 FP8 标签确为软件模拟或误标。
