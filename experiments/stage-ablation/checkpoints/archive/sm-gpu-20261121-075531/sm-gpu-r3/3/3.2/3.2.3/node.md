# N68: 电价敏感性分析：全球主要地区居民/商用电价范围 $0.05-$0.40/kWh；以 $0.15/kWh 为基准，RTX 4090 方案（600W, 10h/da

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

电价敏感性分析：全球主要地区居民/商用电价范围 $0.05-$0.40/kWh；以 $0.15/kWh 为基准，RTX 4090 方案（600W, 10h/day）年电费 $328.5；若电价升至 $0.30/kWh，年电费翻倍至 $657；数据中心方案（700W, 24h/day）在 $0.15/kWh 下年电费 $758.7，在 $0.30/kWh 下为 $1517.4。

## Corrected Claim

电价敏感性分析：全球主要地区居民/商用电价范围 $0.05-$0.40/kWh；以 $0.15/kWh 为基准，RTX 4090 方案（600W, 10h/day）年电费 $328.5；若电价升至 $0.30/kWh，年电费翻倍至 $657；数据中心方案（700W, 24h/day）在 $0.15/kWh 下年电费 $758.7，在 $0.30/kWh 下为 $1517.4。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（600W*10h*365d*0.15$=328.5$；700W*24h*365d*0.15$=758.7$），电价翻倍电费翻倍符合线性关系，全球电价范围符合常识。

## Search Query

average electricity cost per kWh residential commercial 2024 US Europe
