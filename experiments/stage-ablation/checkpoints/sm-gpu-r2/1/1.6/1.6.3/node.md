# N48: 2×RTX 5090 双卡年电力成本：GPU 总 TDP 900W + 系统功耗 200W = 1,100W；24/7 运行年耗电量 1,100W * 24h 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

2×RTX 5090 双卡年电力成本：GPU 总 TDP 900W + 系统功耗 200W = 1,100W；24/7 运行年耗电量 1,100W * 24h * 365d / 1000 = 9,636 kWh；按 $0.1/kWh 电价，年电费 $963.60；若考虑 PUE 1.2，实际电费 $1,156.32。

## Corrected Claim

2×RTX 5090 双卡年电力成本：GPU 总 TDP 900W + 系统功耗 200W = 1,100W；24/7 运行年耗电量 1,100W * 24h * 365d / 1000 = 9,636 kWh；按 $0.1/kWh 电价，年电费 $963.60；若考虑 PUE 1.2，实际电费 $1,156.32。

## Evidence

先验知识/题面给定，逻辑校验通过：功率计算（900+200=1100W）、年耗电量（1.1kW * 8760h = 9636kWh）、电费（9636 * 0.1 = $963.6）及PUE调整（963.6 * 1.2 = $1156.32）均符合物理定律与算术逻辑，数值量级合理。

## Search Query

dual RTX 5090 system power consumption 1100W
