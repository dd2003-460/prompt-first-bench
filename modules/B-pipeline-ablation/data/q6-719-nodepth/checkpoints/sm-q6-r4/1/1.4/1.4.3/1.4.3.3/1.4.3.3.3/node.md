# N717: 混合策略 P99 延迟的计算阈值 x_p99_mix 需满足 F_mix(x_p99_mix) = 0.99，即 P_core * F_core(x_p99_m

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N238

## Claim

混合策略 P99 延迟的计算阈值 x_p99_mix 需满足 F_mix(x_p99_mix) = 0.99，即 P_core * F_core(x_p99_mix) + P_tail * F_tail(x_p99_mix) = 0.99。由于 F_core 和 F_tail 分布不同，x_p99_mix 通常接近于 max(P99_core, P99_tail) 但受 P_core 权重影响，若 P_core=0.6，P99_mix 主要由 F_core 的尾部决定。

## Corrected Claim

混合策略 P99 延迟的计算阈值 x_p99_mix 需满足 F_mix(x_p99_mix) = 0.99，即 P_core * F_core(x_p99_mix) + P_tail * F_tail(x_p99_mix) = 0.99。由于 F_core 和 F_tail 分布不同，x_p99_mix 通常接近于 max(P99_core, P99_tail) 但受 P_core 权重影响，若 P_core=0.6，P99_mix 主要由 F_core 的尾部决定。

## Evidence

先验知识/题面给定，逻辑校验通过：混合分布的分位数定义正确，且当核心权重较大时，混合分位数确实主要由核心分布的尾部决定，符合概率论基本性质。
