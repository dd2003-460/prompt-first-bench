# N13: 硬件精度支持矩阵：NVIDIA Ada Lovelace (RTX 4090) 支持 FP8 和 INT8 加速，Hopper (H100) 支持 FP8 和 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

硬件精度支持矩阵：NVIDIA Ada Lovelace (RTX 4090) 支持 FP8 和 INT8 加速，Hopper (H100) 支持 FP8 和 INT8，Ampere (A100) 仅支持 INT8 和 BF16；需验证所选硬件是否原生支持目标精度以避免软件模拟带来的性能损失。

## Corrected Claim

硬件精度支持矩阵：NVIDIA Ada Lovelace (RTX 4090) 支持 FP8 和 INT8 加速，Hopper (H100) 支持 FP8 和 INT8，Ampere (A100) 仅支持 INT8 和 BF16；需验证所选硬件是否原生支持目标精度以避免软件模拟带来的性能损失。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA Ada Lovelace (RTX 4090) 和 Hopper (H100) 架构确实原生支持 FP8 和 INT8 加速，而 Ampere (A100) 架构主要支持 INT8 和 BF16（FP8 需软件模拟或后续驱动/库支持，非原生硬件单元），陈述符合硬件架构特性。
