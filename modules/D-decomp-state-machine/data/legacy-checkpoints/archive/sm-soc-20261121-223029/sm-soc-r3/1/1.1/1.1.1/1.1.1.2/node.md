# N130: 工作点B（高稳定性/高滞后）：定义窗口 T_window = 30天，统计量 = 中位数，适用条件为 N_deals_30d > 200。此时基准价 P_ref

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

工作点B（高稳定性/高滞后）：定义窗口 T_window = 30天，统计量 = 中位数，适用条件为 N_deals_30d > 200。此时基准价 P_ref_30d 平滑了短期噪声，但在季节性波动（如春节前后）期间可能产生高达 10-15% 的系统性偏差，需引入季节调整因子 S_seasonal。

## Corrected Claim

工作点B（高稳定性/高滞后）：定义窗口 T_window = 30天，统计量 = 中位数，适用条件为 N_deals_30d > 200。此时基准价 P_ref_30d 平滑了短期噪声，但在季节性波动（如春节前后）期间可能产生高达 10-15% 的系统性偏差，需引入季节调整因子 S_seasonal。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

30 day moving median price benchmark seasonal adjustment factor e-commerce
