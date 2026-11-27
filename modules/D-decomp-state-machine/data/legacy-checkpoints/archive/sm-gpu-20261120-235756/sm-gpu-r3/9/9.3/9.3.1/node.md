# N340: MoE 推理的内存访问模式为随机稀疏访问（Random Sparse Access），其有效带宽利用率（Effective Bandwidth Utilizat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129, N130, N131

## Claim

MoE 推理的内存访问模式为随机稀疏访问（Random Sparse Access），其有效带宽利用率（Effective Bandwidth Utilization）远低于密集矩阵乘法（Dense GEMM）的 90-95%，通常仅为 30-50%，这是导致 RTX 5090 FP8 理论峰值无法兑现的核心物理瓶颈，而非计算单元饱和。

## Corrected Claim

MoE 推理的内存访问模式为随机稀疏访问（Random Sparse Access），其有效带宽利用率（Effective Bandwidth Utilization）远低于密集矩阵乘法（Dense GEMM）的 90-95%，通常仅为 30-50%，这是导致 RTX 5090 FP8 理论峰值无法兑现的核心物理瓶颈，而非计算单元饱和。

## Evidence

先验知识/题面给定，逻辑校验通过：MoE推理涉及稀疏专家激活，导致内存访问呈随机稀疏模式，相比密集GEMM的连续访问，其有效带宽利用率显著降低（通常30-50% vs 90-95%），这是GPU推理中常见的物理瓶颈，符合硬件架构基本原理。
