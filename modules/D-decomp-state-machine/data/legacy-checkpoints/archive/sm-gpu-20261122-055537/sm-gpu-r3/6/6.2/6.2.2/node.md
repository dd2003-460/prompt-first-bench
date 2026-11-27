# N97: NVIDIA L4 整机满载功耗基准值 P_draw_L4 为 72W (GPU TDP) + 50W (系统基础功耗，假设低功耗工作站配置) = 122W，来

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

NVIDIA L4 整机满载功耗基准值 P_draw_L4 为 72W (GPU TDP) + 50W (系统基础功耗，假设低功耗工作站配置) = 122W，来源为 NVIDIA L4 数据手册。

## Corrected Claim

NVIDIA L4 GPU TDP 为 72W；在假设低功耗工作站配置（系统基础功耗约 50W）下，整机满载功耗估算约为 122W。

## Evidence

[质询]「系统基础功耗 50W」属于特定硬件配置下的经验估算值，并非 NVIDIA L4 数据手册中定义的固定参数；不同工作站配置（如 CPU 型号、内存数量、硬盘类型）会导致基础功耗显著波动，将其作为固定基准值缺乏严谨性。 | source=knowledge，GPU TDP 72W 符合 NVIDIA L4 官方规格，逻辑自洽；但系统基础功耗 50W 为经验假设值，非手册直接给定，且无外部来源支持该特定配置下的总功耗，故降级。
