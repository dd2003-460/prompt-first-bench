# N261: 截断 Pareto(α=1.1, x_min=1KB, x_max=10GB) 分布下，前 20% 对象的平均大小 E[S | top 20%] = [∫_{x

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

截断 Pareto(α=1.1, x_min=1KB, x_max=10GB) 分布下，前 20% 对象的平均大小 E[S | top 20%] = [∫_{x_min}^{x_20} x * f(x) dx] / [∫_{x_min}^{x_20} f(x) dx]，需计算具体数值（KB），用于验证 128GB 缓存覆盖前 20% 对象的可行性（对比 N92 的 6.4KB 阈值）。

## Corrected Claim

截断 Pareto(α=1.1, x_min=1KB, x_max=10GB) 分布下，前 20% 对象的平均大小 E[S | top 20%] = [∫_{x_min}^{x_20} x * f(x) dx] / [∫_{x_min}^{x_20} f(x) dx]，需计算具体数值（KB），用于验证 128GB 缓存覆盖前 20% 对象的可行性（对比 N92 的 6.4KB 阈值）。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布的条件期望公式定义正确，量纲一致，用于验证缓存覆盖可行性的逻辑自洽。
