# N173: w_speed 在 L < 0.5*L_max 时的边际效应系数：当 L 从 0.5 降至 0.2 时，w_speed 从 0.35 升至 0.42，导致高溢价

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

w_speed 在 L < 0.5*L_max 时的边际效应系数：当 L 从 0.5 降至 0.2 时，w_speed 从 0.35 升至 0.42，导致高溢价商品（P_ask > P_market * 1.2）的曝光量占比 ΔExposure_share 从基线 20% 上升至 35%，具体增量 ΔExposure_share = 0.15 * (1/L - 1/0.5)。

## Corrected Claim

w_speed 在 L < 0.5*L_max 时具有正向边际效应，具体数值关系需依据特定系统文档或实验数据确认。

## Evidence

[质询]该陈述包含具体的经验性数值（如 w_speed 从 0.35 升至 0.42，曝光占比从 20% 升至 35%）以及特定的数学公式（ΔExposure_share = 0.15 * (1/L - 1/0.5)）。这些属于具体的系统参数或经验事实，无法从第一性原理或通用逻辑中严格推导出来，且缺乏任何外部来源支持其具体数值和公式的正确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值和公式）。

## Search Query

dynamic ranking weight adjustment low liquidity second-hand marketplace exposure bias
