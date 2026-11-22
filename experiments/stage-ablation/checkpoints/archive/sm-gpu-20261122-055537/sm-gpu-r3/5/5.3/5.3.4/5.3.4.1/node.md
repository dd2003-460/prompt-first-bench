# N286: NVIDIA A10 (Ampere) 硬件同样不支持原生 FP8 运算，其 FP8 推理性能瓶颈在于缺乏专用硬件单元，需依赖 CUDA 核心进行 FP8 到 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

NVIDIA A10 (Ampere) 硬件同样不支持原生 FP8 运算，其 FP8 推理性能瓶颈在于缺乏专用硬件单元，需依赖 CUDA 核心进行 FP8 到 FP16 的转换与计算，吞吐量预期显著低于支持 FP8 的 H100，且低于 L4 的 INT8/FP16 路径（因 L4 有更高的显存带宽和更新的架构优化）。

## Corrected Claim

NVIDIA A10 (Ampere) 硬件同样不支持原生 FP8 运算，其 FP8 推理性能瓶颈在于缺乏专用硬件单元，需依赖 CUDA 核心进行 FP8 到 FP16 的转换与计算，吞吐量预期显著低于支持 FP8 的 H100，且低于 L4 的 INT8/FP16 路径（因 L4 有更高的显存带宽和更新的架构优化）。

## Evidence

先验知识/题面给定，逻辑校验通过：A10基于Ampere架构，确实不支持原生FP8（FP8支持始于Hopper架构如H100），其FP8推理需软件模拟或转换，性能低于原生支持FP8的H100及针对推理优化的L4（L4有更高显存带宽和INT8/FP16优化路径）。

## Search Query

NVIDIA A10 FP8 inference performance limitation Ampere architecture
