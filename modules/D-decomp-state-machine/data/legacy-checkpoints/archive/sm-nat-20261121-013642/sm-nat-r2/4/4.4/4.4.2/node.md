# N66: 边界条件工作点 2 (高驻留时间)：当 λ_u * T_cold > 5 (即 T_cold > 500 days) 时，C_steady ≈ 1 - exp(

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

边界条件工作点 2 (高驻留时间)：当 λ_u * T_cold > 5 (即 T_cold > 500 days) 时，C_steady ≈ 1 - exp(-5) ≈ 0.993，δ ≈ 1 - 0.993 * (1 - P_hit_cold)。此情形下缓存中几乎全为陈旧对象，命中率完全由 P_hit_cold 决定。

## Corrected Claim

边界条件工作点 2 (高驻留时间)：当 λ_u * T_cold > 5 (即 T_cold > 500 days) 时，C_steady ≈ 1 - exp(-5) ≈ 0.993，δ ≈ 1 - 0.993 * (1 - P_hit_cold)。此情形下缓存中几乎全为陈旧对象，命中率完全由 P_hit_cold 决定。

## Evidence

先验知识/题面给定，逻辑校验通过：指数函数 exp(-5) ≈ 0.0067，1 - 0.0067 ≈ 0.993，数值计算准确；逻辑上，当冷启动时间远大于更新间隔时，缓存中对象确实趋于陈旧，命中率由陈旧对象命中率决定，符合缓存模型直觉。
