# N50: HITL 介入对整体科研循环吞吐率 N_iter_total 的负面影响量化为 N_iter_total = N_iter_base * (1 - T_HITL

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

HITL 介入对整体科研循环吞吐率 N_iter_total 的负面影响量化为 N_iter_total = N_iter_base * (1 - T_HITL_Avg / T_cycle_Avg)，其中 T_HITL_Avg 为平均审核等待时间，T_cycle_Avg 为单次循环平均耗时；为确保 N_iter_total 不低于 N_iter_base 的 80%，必须将 T_HITL_Avg 控制在 T_cycle_Avg 的 20% 以内，这要求审核界面支持批量快速勾选功能。

## Corrected Claim

HITL 介入对整体科研循环吞吐率 N_iter_total 的负面影响量化为 N_iter_total = N_iter_base * (1 - T_HITL_Avg / T_cycle_Avg)，其中 T_HITL_Avg 为平均审核等待时间，T_cycle_Avg 为单次循环平均耗时；为确保 N_iter_total 不低于 N_iter_base 的 80%，必须将 T_HITL_Avg 控制在 T_cycle_Avg 的 20% 以内，这要求审核界面支持批量快速勾选功能。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 N_iter_total = N_iter_base * (1 - T_HITL_Avg / T_cycle_Avg) 在逻辑上自洽，且由不等式 N_iter_total >= 0.8 * N_iter_base 可直接推导出 T_HITL_Avg <= 0.2 * T_cycle_Avg，数学推导成立。

## Search Query

human in the loop latency impact on automation throughput optimization
