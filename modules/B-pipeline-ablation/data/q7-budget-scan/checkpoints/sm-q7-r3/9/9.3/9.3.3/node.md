# N283: 修正后的 SSD 缓存层总功耗 P_SSD = 55 块 * 8.75W ≈ 481W (0.481kW)，远低于 N132 估算的 1.425kW，进一步降低

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

修正后的 SSD 缓存层总功耗 P_SSD = 55 块 * 8.75W ≈ 481W (0.481kW)，远低于 N132 估算的 1.425kW，进一步降低 HDD+SSD 方案的总功耗成本

## Corrected Claim

修正后的 SSD 缓存层总功耗 P_SSD = 55 块 * 8.75W ≈ 481W (0.481kW)，远低于 N132 估算的 1.425kW，进一步降低 HDD+SSD 方案的总功耗成本

## Evidence

先验知识/题面给定，逻辑校验通过：55 * 8.75 = 481.25W，数值计算准确，量级合理，且符合SSD单盘功耗低于HDD的工程常识。
