# N265: 工作点 A（极端重尾）：假设 r_max = 10 * r_min，计算截断 Pareto(β=0.9) 在 [r_min, r_max] 区间内的 C_req

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N93

## Claim

工作点 A（极端重尾）：假设 r_max = 10 * r_min，计算截断 Pareto(β=0.9) 在 [r_min, r_max] 区间内的 C_req(0.1)，量化头部 10% 对象覆盖的请求量比例，验证是否显著高于标准 Pareto 的 0.0105。

## Corrected Claim

工作点 A（极端重尾）：假设 r_max = 10 * r_min，计算截断 Pareto(β=0.9) 在 [r_min, r_max] 区间内的 C_req(0.1)，预期头部 10% 对象覆盖的请求量比例显著高于非截断或轻尾分布下的对应值（具体数值需通过积分计算验证）。

## Evidence

[质询]该陈述包含具体的数值计算结果（0.0105）和比较结论，属于经验/计算事实。由于检索无可用来源，无法验证该特定参数组合（r_max=10*r_min, β=0.9, 截断区间）下的精确数值是否准确，存在计算错误或参数理解偏差的风险。 | 逻辑上，截断Pareto分布的头部集中度确实受β和截断比影响，β=0.9表示重尾，头部占比高是合理的定性趋势；但具体数值0.0105及与'标准Pareto'的对比缺乏来源支持，且'标准Pareto'定义模糊，故降级。

## Search Query

truncated Pareto distribution beta 0.9 top 10 percent request coverage r_max 10 r_min
