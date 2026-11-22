# N383: TCO敏感性分析工作点3（中成本/低功耗-Mac Studio M2 Ultra）：在基准电价$0.15/kWh、硬件价格稳定（ΔP=0）条件下，3年TCO=$

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N135

## Claim

TCO敏感性分析工作点3（中成本/低功耗-Mac Studio M2 Ultra）：在基准电价$0.15/kWh、硬件价格稳定（ΔP=0）条件下，3年TCO=$4,788；当电价上涨ΔE=+100%（$0.30/kWh）时，3年电力成本从$788升至$1,576，总TCO升至$5,576，性价比指标从2.61 tokens/s/$降至2.24 tokens/s/$，排名不变，但因功耗低，在电价>0.30/kWh时相对高功耗方案的TCO优势扩大。

## Corrected Claim

TCO敏感性分析工作点3（中成本/低功耗-Mac Studio M2 Ultra）：在基准电价$0.15/kWh、硬件价格稳定（ΔP=0）条件下，3年TCO=$4,788；当电价上涨ΔE=+100%（$0.30/kWh）时，3年电力成本从$788升至$1,576，总TCO升至$5,576，性价比指标从2.61 tokens/s/$降至2.24 tokens/s/$，排名不变，但因功耗低，在电价>0.30/kWh时相对高功耗方案的TCO优势扩大。

## Evidence

先验知识/题面给定，逻辑校验通过：电力成本翻倍（$788->$1576）导致总TCO增加$788（$4788->$5576），数值自洽；性价比指标随成本增加而下降（2.61->2.24），逻辑合理；Mac Studio M2 Ultra低功耗特性支持其在高电价下相对优势扩大的结论。
