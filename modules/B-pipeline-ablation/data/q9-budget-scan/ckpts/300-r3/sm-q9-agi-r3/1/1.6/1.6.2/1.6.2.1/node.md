# N170: Navier-Stokes 方程在低雷诺数 (Re < 1000) 的 2D 湍流模拟中，使用 FP32 精度 (V100 FP32 13.3 TFLOPS) 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N50

## Claim

Navier-Stokes 方程在低雷诺数 (Re < 1000) 的 2D 湍流模拟中，使用 FP32 精度 (V100 FP32 13.3 TFLOPS) 求解 10^6 网格点，单时间步耗散项的相对误差为 1e-6，经过 1000 步迭代后累积误差为 1e-3 (0.1%)，满足科研级精度要求 (<1%)，无需强制 FP64

## Corrected Claim

Navier-Stokes 方程在低雷诺数 (Re < 1000) 的 2D 湍流模拟中，使用 FP32 精度求解 10^6 网格点，单时间步耗散项的相对误差约为 1e-6。经 1000 步迭代后，若误差线性累积，累积误差约为 1e-3 (0.1%)，满足科研级精度要求 (<1%)；但需注意非线性系统误差可能非线性增长，建议进行误差敏感性分析以确认无需强制 FP64。

## Evidence

[质询]误差累积模型过于简化：将单步相对误差直接乘以步数（1e-6 * 1000 = 1e-3）假设误差线性累积且无相消，忽略了湍流模拟中非线性项导致的误差放大效应及混沌系统的敏感性，实际累积误差可能显著高于线性估算值。 | 先验知识/题面给定，逻辑校验通过但误差累积机制存在不确定性，缺乏外部来源支持具体数值。

## Search Query

Navier-Stokes FP32 vs FP64 error accumulation low Reynolds number CFD simulation precision
