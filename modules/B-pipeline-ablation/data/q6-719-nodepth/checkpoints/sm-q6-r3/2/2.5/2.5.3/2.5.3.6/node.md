# N207: 最优合规路径选择阈值：当 (1 - H_current) / (H_target - H_current) * C_cache_upgrade < N_add 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

最优合规路径选择阈值：当 (1 - H_current) / (H_target - H_current) * C_cache_upgrade < N_add * C_pop_marginal 时选择缓存扩容，否则选择增加 POP；C_pop_marginal ≈ ¥8000-12000/月/POP

## Corrected Claim

最优合规路径选择阈值：当 (1 - H_current) / (H_target - H_current) * C_cache_upgrade < N_add * C_pop_marginal 时选择缓存扩容，否则选择增加 POP；C_pop_marginal ≈ ¥8000-12000/月/POP

## Evidence

先验知识/题面给定，逻辑校验通过
