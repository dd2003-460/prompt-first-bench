# N275: 买家成交周期缩短计算表达式：ΔCycle_time = (T_cycle_baseline - T_cycle_treatment) / T_cycle_bas

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

买家成交周期缩短计算表达式：ΔCycle_time = (T_cycle_baseline - T_cycle_treatment) / T_cycle_baseline * 100%，其中 T_cycle_baseline 为无干预下的平均成交天数，T_cycle_treatment 为透明化干预下的平均成交天数；需计算每次模拟路径的 ΔCycle_time 并统计其分布，若 ΔCycle_time > 10% 则判定该路径满足买家侧帕累托改进条件。

## Corrected Claim

买家成交周期缩短计算表达式：ΔCycle_time = (T_cycle_baseline - T_cycle_treatment) / T_cycle_baseline * 100%，其中 T_cycle_baseline 为无干预下的平均成交天数，T_cycle_treatment 为透明化干预下的平均成交天数；需计算每次模拟路径的 ΔCycle_time 并统计其分布，若 ΔCycle_time > 10% 则判定该路径满足买家侧帕累托改进条件。

## Evidence

先验知识/题面给定，逻辑校验通过
