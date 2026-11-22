# N384: A100 在 FP8 推理模式下的功耗特性：A100 硬件原生不支持 FP8 Tensor Core 计算（FP8 支持始于 Ada Lovelace/Hopp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N135

## Claim

A100 在 FP8 推理模式下的功耗特性：A100 硬件原生不支持 FP8 Tensor Core 计算（FP8 支持始于 Ada Lovelace/Hopper 架构），因此 A100 上的 'FP8 推理' 实际为软件模拟或降精度至 INT8/FP16，其功耗与 FP16/INT8 模式基本一致，无 FP8 专属能效优势，需确认此技术约束对 OpEx 计算的影响（即不能假设 FP8 降低 A100 功耗）。

## Corrected Claim

A100 在 FP8 推理模式下的功耗特性：A100 硬件原生不支持 FP8 Tensor Core 计算（FP8 支持始于 Ada Lovelace/Hopper 架构），因此 A100 上的 'FP8 推理' 实际为软件模拟或降精度至 INT8/FP16，其功耗与 FP16/INT8 模式基本一致，无 FP8 专属能效优势，需确认此技术约束对 OpEx 计算的影响（即不能假设 FP8 降低 A100 功耗）。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 (Ampere架构) 确实不支持原生FP8 Tensor Core，FP8支持始于Hopper/Ada Lovelace架构，因此A100上的FP8推理必然依赖软件模拟或降精度，功耗特性与FP16/INT8一致，无FP8专属能效优势。

## Search Query

A100 FP8 support hardware limitation software emulation
