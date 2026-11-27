# N151: 在更新率独立于对象大小（P_invalidate(s) = 1 - exp(-0.01 * T_res) 恒定）的基准工作点下，字节命中率折损系数 D_byte

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

在更新率独立于对象大小（P_invalidate(s) = 1 - exp(-0.01 * T_res) 恒定）的基准工作点下，字节命中率折损系数 D_bytes 等于时间命中率折损 D_time，即 D_bytes = 1 - P_invalidate ≈ 0.99998（基于平均驻留时间 1/500 天），与对象大小分布无关。

## Corrected Claim

在更新率独立于对象大小（P_invalidate(s) = 1 - exp(-0.01 * T_res) 恒定）的基准工作点下，字节命中率折损系数 D_bytes 等于时间命中率折损 D_time，即 D_bytes = 1 - P_invalidate ≈ 0.99998（基于平均驻留时间 1/500 天），与对象大小分布无关。

## Evidence

先验知识/题面给定，逻辑校验通过：在更新率与对象大小无关的假设下，字节级失效概率与时间级失效概率在统计期望上等价，推导自洽。
