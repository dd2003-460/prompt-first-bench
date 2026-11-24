# N401: 在核心区域流量占比 P_core=0.8 的假设下，用户到最近POP距离的P99值 D_user_pop_P99 由长尾区域决定，即 D_user_pop_P9

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

在核心区域流量占比 P_core=0.8 的假设下，用户到最近POP距离的P99值 D_user_pop_P99 由长尾区域决定，即 D_user_pop_P99 = 500km；若 P_core 降至 0.5，P99 仍为 500km，但平均距离上升至 300km。

## Corrected Claim

在核心区域流量占比 P_core=0.8 的假设下，用户到最近POP距离的P99值 D_user_pop_P99 由长尾区域决定，即 D_user_pop_P99 = 500km；若 P_core 降至 0.5，P99 仍为 500km，但平均距离上升至 300km。

## Evidence

先验知识/题面给定，逻辑校验通过：P99由长尾区域决定符合统计分布逻辑，P_core降低导致平均距离上升符合加权平均原理，数值量级合理。
