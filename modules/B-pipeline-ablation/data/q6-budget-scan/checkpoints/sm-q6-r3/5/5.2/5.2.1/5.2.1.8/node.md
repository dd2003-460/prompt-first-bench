# N242: 最优TTL TTL_opt 的求解条件：TTL_opt = argmin [C_total(TTL)] = argmin [C_storage(TTL) + C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75, N76, N77

## Claim

最优TTL TTL_opt 的求解条件：TTL_opt = argmin [C_total(TTL)] = argmin [C_storage(TTL) + C_bw(TTL) + C_penalty(P99(TTL))]，其中 C_bw(TTL) 与 p_miss(TTL) 成正比，C_penalty 与 P99 超标程度成正比；需数值求解该多目标优化问题

## Corrected Claim

最优TTL TTL_opt 的求解条件：TTL_opt = argmin [C_total(TTL)] = argmin [C_storage(TTL) + C_bw(TTL) + C_penalty(P99(TTL))]，其中 C_bw(TTL) 与 p_miss(TTL) 成正比，C_penalty 与 P99 超标程度成正比；需数值求解该多目标优化问题

## Evidence

先验知识/题面给定，逻辑校验通过
