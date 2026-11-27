# N199: 冷对象驻留时间量化：频率排名 r=100,000 的对象，λ_N ≈ 1 次/天（Pareto 最小值），T_res_N = 1/1 day = 24 小时，表

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

冷对象驻留时间量化：频率排名 r=100,000 的对象，λ_N ≈ 1 次/天（Pareto 最小值），T_res_N = 1/1 day = 24 小时，表明最冷对象在 LRU 中可能驻留一整天

## Corrected Claim

冷对象驻留时间量化：频率排名 r=100,000 的对象，λ_N ≈ 1 次/天（Pareto 最小值），T_res_N = 1/1 day = 24 小时，表明最冷对象在 LRU 中可能驻留一整天

## Evidence

先验知识/题面给定，逻辑校验通过：驻留时间 T_res = 1/λ 是定义上的倒数关系，λ=1次/天对应24小时，量纲与数值自洽。
