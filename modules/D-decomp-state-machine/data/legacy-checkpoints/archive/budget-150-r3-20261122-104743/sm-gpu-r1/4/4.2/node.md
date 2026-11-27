# N20: FP8量化（E4M3或E5M2格式）下Qwen3-27B的显存占用降至约27GB（27B × 1 byte/param），但需硬件原生支持FP8计算单元（如Ho

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

FP8量化（E4M3或E5M2格式）下Qwen3-27B的显存占用降至约27GB（27B × 1 byte/param），但需硬件原生支持FP8计算单元（如Hopper架构H100/H200或Ada Lovelace RTX 4090部分支持），否则需软件模拟导致性能损失

## Corrected Claim

FP8量化（E4M3或E5M2格式）下Qwen3-27B的显存占用降至约27GB（27B × 1 byte/param），但需硬件原生支持FP8计算单元（如Hopper架构H100/H200或Ada Lovelace RTX 4090部分支持），否则需软件模拟导致性能损失

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数×1字节/参数=27GB显存占用符合FP8量化基本计算；H100/H200（Hopper架构）原生支持FP8，RTX 4090（Ada Lovelace）部分支持FP8（主要限于特定操作或需软件辅助），符合硬件架构特性。
