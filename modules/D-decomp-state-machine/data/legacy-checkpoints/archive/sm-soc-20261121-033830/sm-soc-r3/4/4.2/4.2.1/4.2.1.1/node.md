# N220: P_median (同类商品近30天成交中位数) 的计算窗口选择对 P_max 的稳定性有显著影响：若使用30天窗口，P_median 平滑但滞后；若使用7天窗

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

P_median (同类商品近30天成交中位数) 的计算窗口选择对 P_max 的稳定性有显著影响：若使用30天窗口，P_median 平滑但滞后；若使用7天窗口，P_median 灵敏但波动大，需选择窗口长度以平衡价格上限的响应速度与稳定性

## Corrected Claim

P_median (同类商品近30天成交中位数) 的计算窗口选择对 P_max 的稳定性有显著影响：若使用30天窗口，P_median 平滑但滞后；若使用7天窗口，P_median 灵敏但波动大，需选择窗口长度以平衡价格上限的响应速度与稳定性

## Evidence

先验知识/题面给定，逻辑校验通过：时间窗口长度与统计量的平滑度/滞后性/灵敏度/波动性之间的权衡关系符合统计学基本原理（大数定律与方差-偏差权衡），逻辑自洽且无内部矛盾。
