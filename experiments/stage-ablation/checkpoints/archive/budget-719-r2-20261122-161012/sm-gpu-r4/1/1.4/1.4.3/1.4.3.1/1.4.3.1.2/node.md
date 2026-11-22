# N395: Mac Studio M3 Ultra 3 年 24/7 运行电费 (3yr_Electricity_Cost) 修正计算：基于 N290 的 Avg_Powe

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N164

## Claim

Mac Studio M3 Ultra 3 年 24/7 运行电费 (3yr_Electricity_Cost) 修正计算：基于 N290 的 Avg_Power = 325W，3yr_Cost = 325W * 8760h * 3 * $0.15/kWh ≈ $1,287。N164 声称的 $356-$416/年 是基于 350W-400W 峰值计算的年电费，但 24/7 运行应按平均功耗计算。若按峰值 400W 计算，年电费为 $400*8760*0.15 = $525.6，3 年 $1,576.8。因此 N164 的数值偏低，实际 3 年电费约为 $1,287-$1,577 (美国电价)。

## Corrected Claim

Mac Studio M3 Ultra 3 年 24/7 运行电费 (3yr_Electricity_Cost) 修正计算：基于 N290 的 Avg_Power = 325W，3yr_Cost = 325W * 8760h * 3 * $0.15/kWh ≈ $1,287。N164 声称的 $356-$416/年 是基于 350W-400W 峰值计算的年电费，但 24/7 运行应按平均功耗计算。若按峰值 400W 计算，年电费为 $400*8760*0.15 = $525.6，3 年 $1,576.8。因此 N164 的数值偏低，实际 3 年电费约为 $1,287-$1,577 (美国电价)。

## Evidence

先验知识/题面给定，逻辑校验通过：基于325W平均功耗和$0.15/kWh电价的计算（325*8760*3*0.15≈$1287）及基于400W峰值功耗的计算（400*8760*3*0.15≈$1577）在数学上均正确，量级合理。
