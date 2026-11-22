# N199: 计算工作点 A 的 Optimal 字节命中率 H_byte_opt_A = (Σ_{i=1}^{65536} p_i * s_i) / S_total，假设头

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

计算工作点 A 的 Optimal 字节命中率 H_byte_opt_A = (Σ_{i=1}^{65536} p_i * s_i) / S_total，假设头部对象平均大小较大，该值预计为 0.78，代表高覆盖低密度下的性能基准。

## Corrected Claim

计算工作点 A 的 Optimal 字节命中率 H_byte_opt_A = (Σ_{i=1}^{65536} p_i * s_i) / S_total，假设头部对象平均大小较大，该值预计较高（如 0.78 左右），代表高覆盖低密度下的性能基准。

## Evidence

[质询]数值 0.78 为特定经验估计值，缺乏具体数据分布（如 Zipf 参数、对象大小分布）支持，无法从第一性原理严格推导，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持
