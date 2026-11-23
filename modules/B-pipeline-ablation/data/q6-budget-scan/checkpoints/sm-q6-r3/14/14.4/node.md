# N358: 切换成本 C_switch(α) 的量化模型：C_switch(α) = C_migration * |α - α_prev| + C_config * N_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

切换成本 C_switch(α) 的量化模型：C_switch(α) = C_migration * |α - α_prev| + C_config * N_changes，其中 C_migration 为流量切换一次性成本（约 ¥5k-20k/次），C_config 为配置变更成本（约 ¥1k/次），N_changes 为变更次数

## Corrected Claim

切换成本 C_switch(α) 的量化模型：C_switch(α) = C_migration * |α - α_prev| + C_config * N_changes，其中 C_migration 为流量切换一次性成本（约 ¥5k-20k/次），C_config 为配置变更成本（约 ¥1k/次），N_changes 为变更次数

## Evidence

先验知识/题面给定，逻辑校验通过
