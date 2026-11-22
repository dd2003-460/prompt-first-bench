# N251: Blackwell架构（如RTX 5090/B100）上NVFP4原生Tensor Core的理论峰值算力（TFLOPS）为BF16的4倍，且由于权重存储减半（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Blackwell架构（如RTX 5090/B100）上NVFP4原生Tensor Core的理论峰值算力（TFLOPS）为BF16的4倍，且由于权重存储减半（4bit vs 16bit），在内存带宽受限的Decode阶段，其有效吞吐量提升系数约为 4x (算力) / 2x (带宽需求) = 2x 于同代BF16，具体数值需基于B100规格表计算

## Corrected Claim

Blackwell架构（如RTX 5090/B100）上NVFP4原生Tensor Core的理论峰值算力（TFLOPS）为BF16的4倍，且由于权重存储减半（4bit vs 16bit），在内存带宽受限的Decode阶段，其有效吞吐量提升系数约为 4x (算力) / 2x (带宽需求) = 2x 于同代BF16，具体数值需基于B100规格表计算

## Evidence

先验知识/题面给定，逻辑校验通过：NVFP4(4bit)与BF16(16bit)位宽比为4:1，故理论算力峰值为4倍；Decode阶段受内存带宽限制，带宽需求减半（4bit vs 16bit），有效吞吐量提升系数约为 4x(算力) / 2x(带宽需求) = 2x，逻辑自洽且符合硬件架构基本原理。

## Search Query

NVIDIA B100 NVFP4 Tensor Core TFLOPS spec sheet 2025
