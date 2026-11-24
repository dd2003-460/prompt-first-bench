# N507: 自建POP的P99延迟对T_switch的依赖函数 P99_self(T) 在 T ∈ [100, 300]ms 区间内近似为常数 C_self ≈ 150ms

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N168

## Claim

自建POP的P99延迟对T_switch的依赖函数 P99_self(T) 在 T ∈ [100, 300]ms 区间内近似为常数 C_self ≈ 150ms（基于N166及N191），其斜率 d(P99_self)/dT ≈ 0，除非T低于物理极限导致需增加POP数量或改变路由，此时函数发生阶跃变化。

## Corrected Claim

自建POP的P99延迟对T_switch的依赖函数 P99_self(T) 在 T ∈ [100, 300]ms 区间内近似为常数 C_self ≈ 150ms（基于N166及N191），其斜率 d(P99_self)/dT ≈ 0，除非T低于物理极限导致需增加POP数量或改变路由，此时函数发生阶跃变化。

## Evidence

先验知识/题面给定，逻辑校验通过
