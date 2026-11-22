# N82: LFU 冷对象新鲜度失效概率 P_stale_LFU_tail 的精确值：P_stale = 1 - exp(-u_tail * T_res_LFU_tail)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

LFU 冷对象新鲜度失效概率 P_stale_LFU_tail 的精确值：P_stale = 1 - exp(-u_tail * T_res_LFU_tail)，其中 u_tail=0.02/天，T_res_LFU_tail 由 N47 给出；需验证该值是否确实为 0.02 或更低，并对比 LRU 的 P_stale_LRU_tail = 1 - exp(-0.015 * T_res_LRU_tail)

## Corrected Claim

LFU 冷对象新鲜度失效概率 P_stale_LFU_tail 的精确值：P_stale = 1 - exp(-u_tail * T_res_LFU_tail)，其中 u_tail=0.02/天，T_res_LFU_tail 由 N47 给出；需验证该值是否确实为 0.02 或更低，并对比 LRU 的 P_stale_LRU_tail = 1 - exp(-0.015 * T_res_LRU_tail)

## Evidence

先验知识/题面给定，逻辑校验通过
