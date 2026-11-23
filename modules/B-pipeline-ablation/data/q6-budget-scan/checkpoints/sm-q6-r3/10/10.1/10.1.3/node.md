# N335: T_fix硬件更换瓶颈：T_fix = max(T_swapping, T_config_rollback)，其中T_swapping=15min（硬件更换），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

T_fix硬件更换瓶颈：T_fix = max(T_swapping, T_config_rollback)，其中T_swapping=15min（硬件更换），T_config_rollback=10min（配置回滚）；若采用热备节点，T_fix可降至5min（自动切换）

## Corrected Claim

T_fix硬件更换瓶颈：T_fix = max(T_swapping, T_config_rollback)，其中T_swapping=15min（硬件更换），T_config_rollback=10min（配置回滚）；若采用热备节点，T_fix可降至5min（自动切换）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hot standby node failover time vs hardware swapping
