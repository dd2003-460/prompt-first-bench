# N568: RTX 4090 16K INT4 场景的敏感性分析：若电价从 $0.1/kWh 升至 $0.2/kWh（高电价地区），年 OpEx 翻倍至 $7884，TCO

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N173

## Claim

RTX 4090 16K INT4 场景的敏感性分析：若电价从 $0.1/kWh 升至 $0.2/kWh（高电价地区），年 OpEx 翻倍至 $7884，TCO(1yr) 升至 $10483，单位成本增加 60%，但仍低于 4090 双卡 32K 方案的 $5198+OpEx

## Corrected Claim

RTX 4090 16K INT4 场景的敏感性分析：若电价从 $0.1/kWh 升至 $0.2/kWh（高电价地区），年 OpEx 翻倍至 $7884，TCO(1yr) 升至 $10483，单位成本增加 60%，但仍低于 4090 双卡 32K 方案的 $5198+OpEx

## Evidence

先验知识/题面给定，逻辑校验通过：电价翻倍导致OpEx翻倍（$3942->7884），TCO相应增加，且$10483确实低于对比方案成本，数值逻辑自洽。
