# N194: 冷对象驻留时间工作点：频率排名 Bottom 50% 的对象，其访问间隔均值 T_res_cold ≈ 1/λ_cold，其中 λ_cold 由 Pareto(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

冷对象驻留时间工作点：频率排名 Bottom 50% 的对象，其访问间隔均值 T_res_cold ≈ 1/λ_cold，其中 λ_cold 由 Pareto(β=0.9) 尾部积分决定，估算 λ_cold ≈ 10 次/天，T_res_cold ≈ 14.4 小时

## Corrected Claim

冷对象驻留时间工作点：频率排名 Bottom 50% 的对象，其访问间隔均值 T_res_cold ≈ 1/λ_cold，其中 λ_cold 由 Pareto(β=0.9) 尾部积分决定，估算 λ_cold ≈ 10 次/天，T_res_cold ≈ 2.4 小时

## Evidence

先验知识/题面给定，逻辑校验通过：1/10次/天 = 0.1天 = 2.4小时，但题目中写的是14.4小时，这里存在数值计算错误。1/10 = 0.1天 = 2.4小时，而非14.4小时。14.4小时对应的是1/0.0694次/天，即λ≈0.0694次/天，与10次/天不符。因此该陈述存在内部数值矛盾。
