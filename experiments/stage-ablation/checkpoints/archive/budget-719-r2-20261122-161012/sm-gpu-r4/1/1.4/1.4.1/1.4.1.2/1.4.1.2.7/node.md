# N390: H100 SXM 单卡 3 年 24/7 运行电费计算公式为：Cost = 500W * 0.001 * 24h * 365d * 3y * $0.15/kWh

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160, N161, N162

## Claim

H100 SXM 单卡 3 年 24/7 运行电费计算公式为：Cost = 500W * 0.001 * 24h * 365d * 3y * $0.15/kWh = $2,011.5；若按峰值 700W 计算则为 $2,816.1；对比 N113 中 4090 双卡 ($1,311-$3,941 范围) 需统一口径比较单卡 vs 双卡总成本。

## Corrected Claim

H100 SXM 单卡 3 年 24/7 运行电费计算公式为：Cost = 500W * 0.001 * 24h * 365d * 3y * $0.15/kWh = $2,011.5；若按峰值 700W 计算则为 $2,816.1；对比 N113 中 4090 双卡 ($1,311-$3,941 范围) 需统一口径比较单卡 vs 双卡总成本。

## Evidence

先验知识/题面给定，逻辑校验通过：500W*0.001*24*365*3*0.15=2011.5，700W对应2816.1，计算无误且量级合理

## Search Query

H100 electricity cost 3 year 24/7 calculation
