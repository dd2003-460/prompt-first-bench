# N289: 云对象存储扩容的边际硬件成本为零，但边际 API 请求成本随数据量线性增长：若新增 50TB 数据且对象平均大小不变，新增 GET 请求费 = (50TB / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N135

## Claim

云对象存储扩容的边际硬件成本为零，但边际 API 请求成本随数据量线性增长：若新增 50TB 数据且对象平均大小不变，新增 GET 请求费 = (50TB / avg_obj_size) * req_rate * price_per_req，假设 avg_obj_size=1MB, req_rate=2/day, price=¥0.01/万次，则年增成本 ≈ ¥36,500，此为非零的隐性扩容成本。

## Corrected Claim

云对象存储扩容的边际硬件成本为零，但边际 API 请求成本随数据量线性增长：若新增 50TB 数据且对象平均大小不变，新增 GET 请求费 = (50TB / avg_obj_size) * req_rate * price_per_req，假设 avg_obj_size=1MB, req_rate=2/day, price=¥0.01/万次，则年增成本 ≈ ¥36,500，此为非零的隐性扩容成本。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（50*10^6 * 2 * 365 * 0.01/10000 = 36500），且符合云存储按量付费的基本经济逻辑。

## Search Query

cloud object storage scaling marginal API request cost linear growth
