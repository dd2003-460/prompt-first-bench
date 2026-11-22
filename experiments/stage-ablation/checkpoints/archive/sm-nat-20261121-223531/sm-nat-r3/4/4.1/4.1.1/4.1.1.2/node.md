# N150: 更新对象字节占比的精确计算需通过 Pareto(α=1.1) 分布积分：P_byte_upd = ∫_{s_min}^{s_max} s * f_S(s) * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

更新对象字节占比的精确计算需通过 Pareto(α=1.1) 分布积分：P_byte_upd = ∫_{s_min}^{s_max} s * f_S(s) * P(upd|s) ds / E[S]，其中 P(upd|s) 为对象大小为 s 时的更新概率，假设更新率与大小无关，P(upd|s) = λ_upd * Δt，Δt 为时间窗口，在 1 天窗口下 P(upd|s) = 0.01，故 P_byte_upd = 0.01，即 1% 的对象字节被更新。

## Corrected Claim

更新对象字节占比的精确计算需通过 Pareto(α=1.1) 分布积分：P_byte_upd = ∫_{s_min}^{s_max} s * f_S(s) * P(upd|s) ds / E[S]，其中 P(upd|s) 为对象大小为 s 时的更新概率，假设更新率与大小无关，P(upd|s) = λ_upd * Δt，Δt 为时间窗口，在 1 天窗口下 P(upd|s) = 0.01，故 P_byte_upd = 0.01，即 1% 的对象字节被更新。

## Evidence

先验知识/题面给定，逻辑校验通过：在更新概率与对象大小无关的假设下，字节占比的积分计算确实简化为标量概率值，数学推导自洽。
