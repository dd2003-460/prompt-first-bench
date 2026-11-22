# N91: 置信度 80% 的敏感性分析：若 σ_noise² / Var(P_ask) 从 0.2 增加到 0.4，则假设链环节2的预测误差 ΔError = f(0.4

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

置信度 80% 的敏感性分析：若 σ_noise² / Var(P_ask) 从 0.2 增加到 0.4，则假设链环节2的预测误差 ΔError = f(0.4 - 0.2) * Sensitivity_Coeff，其中 Sensitivity_Coeff 为预测模型对噪声方差变化的敏感度系数

## Corrected Claim

置信度 80% 的敏感性分析：若 σ_noise² / Var(P_ask) 从 0.2 增加到 0.4，则假设链环节2的预测误差 ΔError = f(0.4 - 0.2) * Sensitivity_Coeff，其中 Sensitivity_Coeff 为预测模型对噪声方差变化的敏感度系数

## Evidence

先验知识/题面给定，逻辑校验通过
