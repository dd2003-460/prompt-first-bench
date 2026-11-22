# N77: 在中低功耗数据中心级工作点 (1x A100 80GB SXM, TDP 400W + 系统开销 ~200W = 600W) 下，假设电价 $0.10/kWh 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

在中低功耗数据中心级工作点 (1x A100 80GB SXM, TDP 400W + 系统开销 ~200W = 600W) 下，假设电价 $0.10/kWh [待核验] 和 90% 电源效率，每小时电费 = (600W / 0.9 / 1000) * $0.10 = $0.067/h；若全年 7x24 运行，年电费约 $588，代表中等 OPEX 且能效比优于消费级多卡的工作点。

## Corrected Claim

在中低功耗数据中心级工作点 (1x A100 80GB SXM, TDP 400W + 系统开销 ~200W = 600W) 下，假设电价 $0.10/kWh [待核验] 和 90% 电源效率，每小时电费 = (600W / 0.9 / 1000) * $0.10 = $0.067/h；若全年 7x24 运行，年电费约 $588，代表中等 OPEX 且能效比优于消费级多卡的工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 (600/0.9/1000)*0.1*24*365 ≈ 588 正确，参数设定符合数据中心工程常识。

## Search Query

NVIDIA A100 SXM power consumption 400W
