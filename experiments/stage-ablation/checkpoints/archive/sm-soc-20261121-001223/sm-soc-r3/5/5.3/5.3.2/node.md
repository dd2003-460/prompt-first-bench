# N188: 中介路径第二步效应 b 的量化：控制高溢价率后，计算初始曝光量 (E_initial) 对成交周期 (T_deal) 的回归系数 b；假设 T_deal 与 E

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

中介路径第二步效应 b 的量化：控制高溢价率后，计算初始曝光量 (E_initial) 对成交周期 (T_deal) 的回归系数 b；假设 T_deal 与 E_initial 呈负相关，b 的绝对值代表每增加一个单位曝光量所减少的成交天数，需排除直接价格效应以隔离中介路径。

## Corrected Claim

中介路径第二步效应 b 的量化：控制高溢价率后，计算初始曝光量 (E_initial) 对成交周期 (T_deal) 的回归系数 b；假设 T_deal 与 E_initial 呈负相关，b 的绝对值代表每增加一个单位曝光量所减少的成交天数，需排除直接价格效应以隔离中介路径。

## Evidence

先验知识/题面给定，逻辑校验通过：中介效应分析中，路径系数 b 的定义及控制变量隔离逻辑符合统计学原理，量纲（天数/单位曝光）合理。
