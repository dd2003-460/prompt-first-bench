# N139: NVIDIA V100-SXM2 的计算能力为 Compute Capability 7.0 (Volta 架构)，其硬件指令集不支持原生 FP8 (E4M3/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34, N35, N38

## Claim

NVIDIA V100-SXM2 的计算能力为 Compute Capability 7.0 (Volta 架构)，其硬件指令集不支持原生 FP8 (E4M3/E5M2) 数据类型的存储或算术运算，仅支持 FP16, BF16, TF32 和 INT8。

## Corrected Claim

NVIDIA V100-SXM2 的计算能力为 Compute Capability 7.0 (Volta 架构)，其硬件指令集不支持原生 FP8 (E4M3/E5M2) 数据类型的存储或算术运算，仅支持 FP16, BF16, TF32 和 INT8。

## Evidence

先验知识/题面给定，逻辑校验通过：V100基于Volta架构（CC 7.0），其Tensor Core仅支持FP16/BF16/INT8/TF32，FP8支持始于Hopper架构（H100, CC 9.0），故V100不支持FP8符合硬件事实。

## Search Query

NVIDIA V100 compute capability 7.0 supported data types FP8 hardware support
