# N264: 工作点 C（乐观/低成本）：假设 Pareto 截断 x_max = 1MB，计算 E[S | top 20%]，若显著小于 6.4KB，则 128GB 缓存可

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

工作点 C（乐观/低成本）：假设 Pareto 截断 x_max = 1MB，计算 E[S | top 20%]，若显著小于 6.4KB，则 128GB 缓存可覆盖前 20% 且余量充足，此时命中率下界接近理论最大值，需量化余量对驱逐抖动的影响。

## Corrected Claim

工作点 C（乐观/低成本）：假设 Pareto 截断 x_max 为特定值（如 1MB），计算 E[S | top 20%]，若该值显著小于缓存行大小或特定阈值（如 6.4KB），则 128GB 缓存可覆盖前 20% 且余量充足，此时命中率下界接近理论最大值，需量化余量对驱逐抖动的影响。

## Evidence

[质询]该陈述包含具体的经验性数值假设（x_max=1MB, 6.4KB, 128GB），这些参数无法从第一性原理推导，且缺乏外部来源支持其合理性或具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

small object cache coverage Pareto distribution truncated 1MB mean size calculation
