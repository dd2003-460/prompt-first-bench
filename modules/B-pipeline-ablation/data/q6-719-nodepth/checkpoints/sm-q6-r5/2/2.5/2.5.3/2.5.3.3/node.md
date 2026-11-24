# N204: 迭代求解 N_add 的收敛边界：当 L_p99_current - T_target < ΔL_per_pop(N_pop + N_add) 时停止，若初始缺

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64, N65, N66

## Claim

迭代求解 N_add 的收敛边界：当 L_p99_current - T_target < ΔL_per_pop(N_pop + N_add) 时停止，若初始缺口 > 50ms 且 T_target < 80ms，则需 N_add ≥ 3 才能满足约束

## Corrected Claim

迭代求解 N_add 的收敛边界：当 L_p99_current - T_target < ΔL_per_pop(N_pop + N_add) 时停止。具体所需的 N_add 数值取决于初始缺口、目标延迟及单次 pop 的延迟增量，需根据实际系统参数计算确定。

## Evidence

父节点级核验未通过：不完备（子节点分别描述了延迟改善机制（边际降低量）和容量承载约束（带宽/CPU），二者正交且不冗余。但父节点明确提出了基于初始缺口（>50ms）和目标延迟（<80ms）的启发式规则（需 N_add ≥ 3），子节点仅提供了通用的解析近似和容量下界，未涵盖这一具体的收敛停止逻辑或阈值判断条件，导致完备性不足。）
