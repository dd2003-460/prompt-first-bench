# N78: 计算低频对象占比：Pareto(β=0.9)中，请求率 r < 1/100 day 的对象比例。设 r_min 为最小请求率，r_max 为最大请求率。累积分布

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

计算低频对象占比：Pareto(β=0.9)中，请求率 r < 1/100 day 的对象比例。设 r_min 为最小请求率，r_max 为最大请求率。累积分布函数 CDF(r) = (r_min/r)^{β-1}。需计算 r < r_threshold = 1/100 的积分比例。若 r_min 极小，则大部分长尾对象满足此条件，导致整体有效命中率显著低于100%。

## Corrected Claim

计算低频对象占比：Pareto(β=0.9)中，请求率 r < 1/100 day 的对象比例。设 r_min 为最小请求率，r_max 为最大请求率。累积分布函数 CDF(r) = (r_min/r)^{β-1}。需计算 r < r_threshold = 1/100 的积分比例。若 r_min 极小，则大部分长尾对象满足此条件，导致整体有效命中率显著低于100%。

## Evidence

父节点级核验未通过：不完备（子节点仅计算了低频对象的字节流量占比（P_bytes），而父节点明确要求计算的是“对象比例”（即满足 r < r_threshold 的对象数量占比或积分比例）。两者定义不同（一个是对象计数/概率质量，一个是字节加权流量），子节点未能覆盖父节点的核心定义。）
