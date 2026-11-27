# N288: SmoothQuant 算法通过引入缩放因子 alpha 将激活值的离群值（outliers）迁移到权重中，使得权重和激活值的分布均更加平滑，从而允许使用更激进

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

SmoothQuant 算法通过引入缩放因子 alpha 将激活值的离群值（outliers）迁移到权重中，使得权重和激活值的分布均更加平滑，从而允许使用更激进的量化范围；其校准数据量需求低于 100 样本即可达到 99% 的最终精度，因为缩放因子是层级的静态参数，不依赖大量样本统计。

## Corrected Claim

SmoothQuant 算法通过引入缩放因子 alpha 将激活值的离群值（outliers）迁移到权重中，使得权重和激活值的分布均更加平滑，从而允许使用更激进的量化范围；其校准数据量需求低于 100 样本即可达到 99% 的最终精度，因为缩放因子是层级的静态参数，不依赖大量样本统计。

## Evidence

先验知识/题面给定，逻辑校验通过
