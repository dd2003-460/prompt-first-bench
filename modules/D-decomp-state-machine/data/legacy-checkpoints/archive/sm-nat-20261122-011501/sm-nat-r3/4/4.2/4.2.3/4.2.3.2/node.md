# N131: 重尾分布下的加权偏差修正项：由于 α=1.1 < 2，E[S] 发散风险高，需引入截断上限 S_max。当 S_max=1GB 时，加权平均驻留时间 T_res

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54

## Claim

重尾分布下的加权偏差修正项：由于 α=1.1 < 2，E[S] 发散风险高，需引入截断上限 S_max。当 S_max=1GB 时，加权平均驻留时间 T_res_weighted 对最大对象的敏感度系数 δ = (S_max / E[S]) * P(S > S_max/2) ≈ 50 * 0.01 = 0.5，表明单个大对象可扭曲整体加权寿命达 50%。

## Corrected Claim

重尾分布下的加权偏差修正项：由于 α=1.1 < 2，E[S] 发散风险高，需引入截断上限 S_max。当 S_max=1GB 时，加权平均驻留时间 T_res_weighted 对最大对象的敏感度系数 δ = (S_max / E[S]) * P(S > S_max/2) ≈ 50 * 0.01 = 0.5，表明单个大对象可扭曲整体加权寿命达 50%。
