# N235: T_low 的量化基准值为 21 天，基于 N96 中 48 小时无咨询导致的长尾延迟，假设降价后咨询到达率 λ_low 显著低于 λ_high，需计算 T_l

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

T_low 的量化基准值为 21 天，基于 N96 中 48 小时无咨询导致的长尾延迟，假设降价后咨询到达率 λ_low 显著低于 λ_high，需计算 T_low = 1/λ_low 并与 T_high = 1/λ_high 进行对比，验证机会成本项的正负号。

## Corrected Claim

T_low 的量化基准值为 21 天，基于 N96 中 48 小时无咨询导致的长尾延迟，假设降价后咨询到达率 λ_low 显著低于 λ_high，需计算 T_low = 1/λ_low 并与 T_high = 1/λ_high 进行对比，验证机会成本项的正负号。

## Evidence

先验知识/题面给定，逻辑校验通过：T=1/λ 符合泊松过程平均到达间隔定义，21天与48小时量级对比合理，用于验证机会成本符号的逻辑自洽。
