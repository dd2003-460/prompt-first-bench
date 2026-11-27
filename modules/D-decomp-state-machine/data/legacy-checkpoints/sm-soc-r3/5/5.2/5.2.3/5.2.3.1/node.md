# N268: 敏感度系数 Sensitivity_Coeff 的解析推导：在假设链环节2（价格-转化回归）中，Sensitivity_Coeff ≈ |∂β_info/∂σ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

敏感度系数 Sensitivity_Coeff 的解析推导：在假设链环节2（价格-转化回归）中，Sensitivity_Coeff ≈ |∂β_info/∂σ_noise²| = β_info / (2 * σ_noise²)，当 σ_noise²/Var(P_ask) 从 0.2 增至 0.4 时，ΔError ≈ β_info * 0.2 / (2 * 0.2 * Var(P_ask)) * 0.2，需代入具体 β_info 值计算。

## Corrected Claim

敏感度系数 Sensitivity_Coeff 的解析推导：在假设链环节2（价格-转化回归）中，Sensitivity_Coeff ≈ |∂β_info/∂σ_noise²| = β_info / (2 * σ_noise²)，当 σ_noise²/Var(P_ask) 从 0.2 增至 0.4 时，ΔError ≈ β_info * 0.2 / (2 * 0.2 * Var(P_ask)) * 0.2，需代入具体 β_info 值计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

sensitivity analysis of regression coefficients to noise variance in econometric models
