# N151: 静态权重锁定期的置信度修正系数 C_static：在 T_update > 7 天的窗口内，定义 C_static = 1 - (T_observed / T_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

静态权重锁定期的置信度修正系数 C_static：在 T_update > 7 天的窗口内，定义 C_static = 1 - (T_observed / T_update) * Sensitivity_Algo，其中 T_observed 为观察窗口长度（如 3 天），Sensitivity_Algo 为算法动态调整对均衡稳定性的敏感系数（假设 0.1/day），用于量化因排除近期迭代干扰而保留的置信度比例。

## Corrected Claim

静态权重锁定期的置信度修正系数 C_static：在 T_update > 7 天的窗口内，定义 C_static = 1 - (T_observed / T_update) * Sensitivity_Algo，其中 T_observed 为观察窗口长度（如 3 天），Sensitivity_Algo 为算法动态调整对均衡稳定性的敏感系数（假设 0.1/day），用于量化因排除近期迭代干扰而保留的置信度比例。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

algorithm dynamic adjustment sensitivity coefficient equilibrium stability confidence correction
