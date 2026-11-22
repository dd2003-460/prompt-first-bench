# N324: T_delay 的分布形态检验：通过 Kolmogorov-Smirnov 检验（KS 统计量 D = max|F_empirical(x) - F_theor

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102, N103, N104

## Claim

T_delay 的分布形态检验：通过 Kolmogorov-Smirnov 检验（KS 统计量 D = max|F_empirical(x) - F_theoretical(x)|）判断 T_delay 是否服从指数分布（记忆lessness 性质）；若 KS 检验 p 值 < 0.05，则拒绝指数分布假设，表明买家惰性存在时间依赖性（如周末效应），此时 T_delay > 48 hours 的判定需按星期几分层计算，否则阈值 τ_anomaly 的交互效应会被平均效应掩盖。

## Corrected Claim

T_delay 的分布形态检验：通过 Kolmogorov-Smirnov 检验（KS 统计量 D = max|F_empirical(x) - F_theoretical(x)|）判断 T_delay 是否服从指数分布（记忆lessness 性质）；若 KS 检验 p 值 < 0.05，则拒绝指数分布假设，表明买家惰性存在时间依赖性（如周末效应），此时 T_delay > 48 hours 的判定需按星期几分层计算，否则阈值 τ_anomaly 的交互效应会被平均效应掩盖。

## Evidence

先验知识/题面给定，逻辑校验通过：KS检验用于分布形态检验，p<0.05拒绝原假设，指数分布对应无记忆性，若存在时间依赖性（如周末效应）则需分层计算以避免交互效应被平均掩盖，逻辑自洽且符合统计学原理。

## Search Query

Kolmogorov-Smirnov test exponential distribution user behavior delay
