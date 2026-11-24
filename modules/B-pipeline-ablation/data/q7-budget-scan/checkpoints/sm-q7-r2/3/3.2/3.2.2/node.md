# N89: HDD待机功耗与活跃功耗差异显著，冷数据80%时间处于待机状态，平均功耗可按 (0.8*待机功耗 + 0.2*活跃功耗) 计算，进一步降低电费估算。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

HDD待机功耗与活跃功耗差异显著，冷数据80%时间处于待机状态，平均功耗可按 (0.8*待机功耗 + 0.2*活跃功耗) 计算，进一步降低电费估算。

## Corrected Claim

HDD待机功耗与活跃功耗差异显著，冷数据80%时间处于待机状态，平均功耗可按 (0.8*待机功耗 + 0.2*活跃功耗) 计算，进一步降低电费估算。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式在数学上自洽，且HDD待机功耗显著低于活跃功耗符合物理事实，冷数据低访问频率导致高待机占比符合存储工程常识。

## Search Query

HDD idle power vs active power average consumption
