# N122: 公有云 CDN 带宽成本归一化：月成本转换为每千请求成本 Cost_per_1k_req = (Monthly_Cost × 12) / (R_total_an

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

公有云 CDN 带宽成本归一化：月成本转换为每千请求成本 Cost_per_1k_req = (Monthly_Cost × 12) / (R_total_annual / 1000)，基于阿里云 10,800 元/月，年成本 = 129,600 元，每千请求成本 = 129,600 / 394,595 ≈ 0.329 元/千请求

## Corrected Claim

公有云 CDN 带宽成本归一化：月成本转换为每千请求成本 Cost_per_1k_req = (Monthly_Cost × 12) / (R_total_annual / 1000)，基于阿里云 10,800 元/月，年成本 = 129,600 元，每千请求成本 = 129,600 / 394,595 ≈ 0.329 元/千请求

## Evidence

先验知识/题面给定，逻辑校验通过：10,800 * 12 = 129,600；129,600 / 394,595 ≈ 0.3284，四舍五入为 0.329，计算无误。
