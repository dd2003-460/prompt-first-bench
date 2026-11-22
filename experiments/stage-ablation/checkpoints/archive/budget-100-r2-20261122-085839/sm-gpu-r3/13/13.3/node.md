# N345: Mac Studio (M3 Max, 128GB) 的系统级 TDP 约为 100-150W (满载)，在 24/7 运行场景下，年电力成本 = 150W *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

Mac Studio (M3 Max, 128GB) 的系统级 TDP 约为 100-150W (满载)，在 24/7 运行场景下，年电力成本 = 150W * 8760h / 1000 * $0.12/kWh = $157.68/年；相比 RTX 4090 方案节省 $316.44/年，电力成本优势显著，但需结合硬件采购价 ($4,000-$5,000) 计算总 TCO。

## Corrected Claim

Mac Studio (M3 Max, 128GB) 的系统级 TDP 约为 100-150W (满载)，在 24/7 运行场景下，年电力成本 = 150W * 8760h / 1000 * $0.12/kWh = $157.68/年；相比 RTX 4090 方案节省 $316.44/年，电力成本优势显著，但需结合硬件采购价 ($4,000-$5,000) 计算总 TCO。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Max 128GB 版本满载功耗确实在 100-150W 区间（通常约 150W 上限），RTX 4090 方案（含 CPU 等）功耗通常远高于此（约 400-500W+），计算逻辑自洽，数值量级合理。

## Search Query

Mac Studio M3 Max power consumption TDP watts
