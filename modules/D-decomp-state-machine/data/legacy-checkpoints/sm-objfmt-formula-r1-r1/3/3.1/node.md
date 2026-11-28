# N13: 单卡与多卡方案的初始采购成本(TCO_Initial)对比模型：Cost_Initial = Num_GPUs * Price_Per_GPU + (Num_G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

单卡与多卡方案的初始采购成本(TCO_Initial)对比模型：Cost_Initial = Num_GPUs * Price_Per_GPU + (Num_GPUs > 1 ? Motherboard_CPU_RAM_Overhead : 0)，需量化多卡平台额外主板/电源/CPU成本

## Corrected Claim

单卡与多卡方案的初始采购成本(TCO_Initial)对比模型：Cost_Initial = Num_GPUs * Price_Per_GPU + (Num_GPUs > 1 ? Motherboard_CPU_RAM_Overhead : 0)，需量化多卡平台额外主板/电源/CPU成本

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-GPU workstation motherboard CPU power supply additional cost vs single GPU
