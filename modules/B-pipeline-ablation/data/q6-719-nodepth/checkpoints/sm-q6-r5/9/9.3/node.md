# N126: 惩罚项的非线性修正：实际用户流失并非线性，存在阈值效应；当 L_p99 < T_target 时 C_penalty = 0，当 T_target ≤ L_p9

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

惩罚项的非线性修正：实际用户流失并非线性，存在阈值效应；当 L_p99 < T_target 时 C_penalty = 0，当 T_target ≤ L_p99 < T_threshold (T_target + 100ms) 时 C_penalty 呈二次增长，超过 T_threshold 后呈指数增长（用户直接卸载 APP）。

## Corrected Claim

惩罚项的非线性修正：实际用户流失并非线性，存在阈值效应；当 L_p99 < T_target 时 C_penalty = 0，当 T_target ≤ L_p99 < T_threshold (T_target + 100ms) 时 C_penalty 呈二次增长，超过 T_threshold 后呈指数增长（用户直接卸载 APP）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

user retention threshold latency nonlinear churn model mobile app
