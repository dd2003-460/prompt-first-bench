# N90: NVFP4 硬件支持现状：目前仅 NVIDIA Blackwell 架构（RTX 50xx 系列及 B100/B200）原生支持 FP4 推理加速，RTX 40

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

NVFP4 硬件支持现状：目前仅 NVIDIA Blackwell 架构（RTX 50xx 系列及 B100/B200）原生支持 FP4 推理加速，RTX 4090/5090 需通过软件模拟或特定 CUDA 内核实现，性能损耗约 30-50% [待核验具体基准测试数据]

## Corrected Claim

NVFP4 硬件支持现状：NVIDIA Blackwell 架构（包括 RTX 50xx 系列及 B100/B200）原生支持 FP4 推理加速；前代架构（如 RTX 40xx）需通过软件模拟或特定 CUDA 内核实现，具体性能损耗取决于工作负载和实现方式，缺乏统一基准数据。

## Evidence

[质询]RTX 5090 基于 Blackwell 架构，通常原生支持 FP4，将其归类为需软件模拟且性能损耗 30-50% 与硬件架构特性相悖；此外，30-50% 的具体损耗数值缺乏公开基准测试支持，属于未经证实的经验数据。 | 无可用外部证据；逻辑上 RTX 5090 作为 Blackwell 架构显卡应原生支持 FP4，原陈述将其归入非原生支持类别存在事实错误风险，且具体性能损耗数值缺乏来源支持，故降级。

## Search Query

NVIDIA Blackwell FP4 inference performance penalty vs native support RTX 5090
