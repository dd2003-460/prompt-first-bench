# N132: 触发云端升级的成本阈值计算：设云端 API 单次完整任务成本为 C_cloud (约 $0.5-$2)，本地人工干预成本为 C_human (100元≈$14)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

触发云端升级的成本阈值计算：设云端 API 单次完整任务成本为 C_cloud (约 $0.5-$2)，本地人工干预成本为 C_human (100元≈$14)，若 Blocked 率 P_block > 20%，则期望成本 E_cost = P_block * C_human + (1-P_block) * C_local；当 E_cost > C_cloud * 1.5 时，应直接路由至云端而非尝试本地修复，以规避隐性时间成本。

## Corrected Claim

触发云端升级的成本阈值计算：设云端 API 单次完整任务成本为 C_cloud (约 $0.5-$2)，本地人工干预成本为 C_human (100元≈$14)，若 Blocked 率 P_block > 20%，则期望成本 E_cost = P_block * C_human + (1-P_block) * C_local；当 E_cost > C_cloud * 1.5 时，应直接路由至云端而非尝试本地修复，以规避隐性时间成本。

## Evidence

先验知识/题面给定，逻辑校验通过
