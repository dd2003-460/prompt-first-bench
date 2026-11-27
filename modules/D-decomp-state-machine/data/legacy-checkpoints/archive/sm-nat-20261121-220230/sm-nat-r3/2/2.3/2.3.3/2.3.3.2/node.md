# N157: LFU 指数衰减因子 λ_decay = 1/7 天的理论依据：基于热度半衰期 T_half = ln(2)/λ_decay ≈ 4.85 天，该值需满足 T_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

LFU 指数衰减因子 λ_decay = 1/7 天的理论依据：基于热度半衰期 T_half = ln(2)/λ_decay ≈ 4.85 天，该值需满足 T_half > T_resident_hot (0.5天) 且 T_half < T_stability_cold (3.0天) 以平衡记忆与响应；若 λ_decay 偏离 1/7 超过 ±20%，LFU 增益将下降超过 1.5%。

## Corrected Claim

LFU 指数衰减因子 λ_decay = 1/7 天的理论依据：基于热度半衰期 T_half = ln(2)/λ_decay ≈ 4.85 天，该值需满足 T_half > T_resident_hot (0.5天) 且 T_half < T_stability_cold (3.0天) 以平衡记忆与响应；若 λ_decay 偏离 1/7 超过 ±20%，LFU 增益将下降超过 1.5%。
