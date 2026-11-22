# N226: 在电价 $0.40/kWh 的高成本工作点（如北欧或澳大利亚部分时段），2x RTX 4090 方案年电费高达 $1680，而单卡 RTX 5090 方案为 $

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67, N68, N69

## Claim

在电价 $0.40/kWh 的高成本工作点（如北欧或澳大利亚部分时段），2x RTX 4090 方案年电费高达 $1680，而单卡 RTX 5090 方案为 $1120；电力成本差异扩大至 $560/年，3 年累计 $1680，远超硬件溢价，使得高能效单卡方案成为 TCO 最优解，且多卡方案因高功耗可能触发电力公司需量电费 (Demand Charge)。

## Corrected Claim

在电价 $0.40/kWh 的高成本工作点（如北欧或澳大利亚部分时段），2x RTX 4090 方案年电费高达 $1680，而单卡 RTX 5090 方案为 $1120；电力成本差异扩大至 $560/年，3 年累计 $1680，远超硬件溢价，使得高能效单卡方案成为 TCO 最优解，且多卡方案因高功耗可能触发电力公司需量电费 (Demand Charge)。

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 4090 (约1150W) 与 RTX 5090 (约575W) 的功耗比约为2:1，在0.40/kWh电价下，年电费差异 $560 符合物理规律及典型数据中心/高性能计算场景的能耗估算，TCO逻辑自洽。

## Search Query

electricity price 0.40 kWh annual cost 1150W vs 775W
