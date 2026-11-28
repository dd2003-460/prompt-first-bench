# N644: 工作点2（激进估算/低 PUE 场景）：假设高效冷却环境 PUE = 1.2 且忽略部分静态功耗，4x V100 集群总功耗 P_total_aggressiv

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N230

## Claim

工作点2（激进估算/低 PUE 场景）：假设高效冷却环境 PUE = 1.2 且忽略部分静态功耗，4x V100 集群总功耗 P_total_aggressive ≈ 840W（700W * 1.2），对应月度电费（按 $0.35/kWh, 720h）为 $211.7，此值用于乐观预算规划与实际能耗监控基准。

## Corrected Claim

工作点2（激进估算/低 PUE 场景）：假设高效冷却环境 PUE = 1.2 且忽略部分静态功耗，4x V100 集群总功耗 P_total_aggressive ≈ 840W（700W * 1.2），对应月度电费（按 $0.35/kWh, 720h）为 $211.7，此值用于乐观预算规划与实际能耗监控基准。

## Evidence

先验知识/题面给定，逻辑校验通过：700W * 1.2 = 840W，840W * 720h * $0.35/kWh = $211.68 ≈ $211.7，计算无误且符合物理直觉。
