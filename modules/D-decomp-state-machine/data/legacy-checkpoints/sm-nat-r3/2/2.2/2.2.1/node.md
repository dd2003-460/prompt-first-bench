# N49: 对象 i 的访问间隔分布：对于 Pareto(β=0.9) 热度分布，对象 i 的请求间隔 T_i 服从指数分布，其均值 E[T_i] = 1 / λ_i，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

对象 i 的访问间隔分布：对于 Pareto(β=0.9) 热度分布，对象 i 的请求间隔 T_i 服从指数分布，其均值 E[T_i] = 1 / λ_i，其中 λ_i = r_i * (5000万/天) / N_total，r_i 为对象 i 的相对热度。

## Corrected Claim

对象 i 的访问间隔分布：对于 Pareto(β=0.9) 热度分布，对象 i 的请求间隔 T_i 服从指数分布，其均值 E[T_i] = 1 / λ_i，其中 λ_i = r_i * (5000万/天) / N_total，r_i 为对象 i 的相对热度。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义热度分布（输入参数），节点2推导绝对速率（中间计算），节点3计算最终间隔（输出结果）。三者无重复，无矛盾，共同覆盖了从分布定义到最终均值计算的完整链条，符合父节点描述。）
