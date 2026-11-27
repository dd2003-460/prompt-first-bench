# N125: 更新失效与容量驱逐的边界条件：当 R_req_update < 1 时，更新失效成为主导因素，此时 F_decay 不再近似为 1，而需使用 F_decay =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N46

## Claim

更新失效与容量驱逐的边界条件：当 R_req_update < 1 时，更新失效成为主导因素，此时 F_decay 不再近似为 1，而需使用 F_decay = 1 - u * T_resident * H_LRU；临界更新率 u_crit = 1 / T_resident；基于 N34，T_resident ≈ 1.55e-5 天，故 u_crit ≈ 64500/天；当前 u=0.01/天 << u_crit，故系统深处'容量驱逐主导'区域，更新失效的影响可忽略（< 0.001%）。

## Corrected Claim

更新失效与容量驱逐的边界条件：当 R_req_update < 1 时，更新失效成为主导因素，此时 F_decay 不再近似为 1，而需使用 F_decay = 1 - u * T_resident * H_LRU；临界更新率 u_crit = 1 / T_resident；基于 N34，T_resident ≈ 1.55e-5 天，故 u_crit ≈ 64500/天；当前 u=0.01/天 << u_crit，故系统深处'容量驱逐主导'区域，更新失效的影响可忽略（< 0.001%）。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（1/1.55e-5 ≈ 64516），量级对比合理（0.01 << 64500），推导逻辑自洽。
