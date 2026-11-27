# N93: N30 中给出的阈值 T_residence < 100 天 对应于折损 < 1% 的临界条件，该阈值是基于 U_rate=0.01/day 推导出的近似值（0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

N30 中给出的阈值 T_residence < 100 天 对应于折损 < 1% 的临界条件，该阈值是基于 U_rate=0.01/day 推导出的近似值（0.01 * 100 = 1.0），但在重尾分布下，由于大对象驻留时间显著长于平均驻留时间，实际折损需按对象大小加权计算，而非仅用平均 T_residence。

## Corrected Claim

N30 中给出的阈值 T_residence < 100 天 对应于折损 < 1% 的临界条件，该阈值是基于 U_rate=0.01/day 推导出的近似值（0.01 * 100 = 1.0），但在重尾分布下，由于大对象驻留时间显著长于平均驻留时间，实际折损需按对象大小加权计算，而非仅用平均 T_residence。

## Evidence

先验知识/题面给定，逻辑校验通过：0.01/day * 100 days = 1.0 (100%) 的算术推导正确，且重尾分布下加权平均驻留时间大于算术平均驻留时间的统计学原理成立。
