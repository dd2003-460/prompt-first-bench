# N202: 低解释力工作点：当 Var(P_markup | λ) / Var(P_markup_total) < 0.5 时，噪声主导，需引入其他噪声项（如买家随机偏好 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

低解释力工作点：当 Var(P_markup | λ) / Var(P_markup_total) < 0.5 时，噪声主导，需引入其他噪声项（如买家随机偏好 σ_noise_buyer²、平台算法波动 σ_algo²）；置信度降至 0.6，且需满足 σ_noise_buyer² + σ_algo² > 0.5 * Var(P_markup_total)，否则模型不可识别。

## Corrected Claim

低解释力工作点：当 Var(P_markup | λ) / Var(P_markup_total) < 0.5 时，噪声主导，需引入其他噪声项（如买家随机偏好 σ_noise_buyer²、平台算法波动 σ_algo²）；置信度降至 0.6，且需满足 σ_noise_buyer² + σ_algo² > 0.5 * Var(P_markup_total)，否则模型不可识别。

## Evidence

先验知识/题面给定，逻辑校验通过
