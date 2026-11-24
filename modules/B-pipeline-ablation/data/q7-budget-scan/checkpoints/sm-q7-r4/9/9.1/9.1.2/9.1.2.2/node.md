# N662: SSD 缓存层单盘加权平均功耗 W_SSD_avg 修正：基于 N282 的工作负载模型（50% Active Read/Write @ 15W, 50% Id

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N275

## Claim

SSD 缓存层单盘加权平均功耗 W_SSD_avg 修正：基于 N282 的工作负载模型（50% Active Read/Write @ 15W, 50% Idle @ 2.5W），但需采纳 N265 对空闲功耗的修正（Idle ≈ 1.2W，非 2.5W）。修正后 W_SSD_avg = 0.5 * 15W + 0.5 * 1.2W = 8.1W。若采用更保守的 60/40 活跃/空闲比例，W_SSD_avg = 0.6 * 15 + 0.4 * 1.2 = 9.48W。

## Corrected Claim

SSD 缓存层单盘加权平均功耗 W_SSD_avg 修正：基于 N282 的工作负载模型（50% Active Read/Write @ 15W, 50% Idle @ 2.5W），但需采纳 N265 对空闲功耗的修正（Idle ≈ 1.2W，非 2.5W）。修正后 W_SSD_avg = 0.5 * 15W + 0.5 * 1.2W = 8.1W。若采用更保守的 60/40 活跃/空闲比例，W_SSD_avg = 0.6 * 15 + 0.4 * 1.2 = 9.48W。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（0.5*15+0.5*1.2=8.1; 0.6*15+0.4*1.2=9.48），功耗量级符合SSD典型规格，内部逻辑自洽。
