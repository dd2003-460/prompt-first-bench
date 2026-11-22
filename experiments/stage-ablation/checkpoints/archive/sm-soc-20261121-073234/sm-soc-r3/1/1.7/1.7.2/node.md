# N48: 成交基准 C_t 的动态更新机制：C_t 并非静态常数，而是随时间窗口滑动的移动中位数，其更新频率（如每日/每周）和窗口长度（如7天/30天）直接影响 P_t 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N11

## Claim

成交基准 C_t 的动态更新机制：C_t 并非静态常数，而是随时间窗口滑动的移动中位数，其更新频率（如每日/每周）和窗口长度（如7天/30天）直接影响 P_t - C_t 的偏差大小，需量化不同窗口长度下 C_t 的滞后误差方差。

## Corrected Claim

成交基准 C_t 的动态更新机制：C_t 并非静态常数，而是随时间窗口滑动的移动中位数，其更新频率（如每日/每周）和窗口长度（如7天/30天）直接影响 P_t - C_t 的偏差大小，需量化不同窗口长度下 C_t 的滞后误差方差。

## Evidence

先验知识/题面给定，逻辑校验通过：移动中位数作为动态基准在金融和统计领域是标准做法，窗口长度与滞后误差方差的正相关关系符合时间序列分析的基本原理。

## Search Query

moving median window length impact on price benchmark lag error variance
