# N694: 公有云CDN请求数成本在高流量工作点（月请求量 50亿次，对应DAU 500万/日均333次请求的高频短视频场景）的量化值：Cloud_Request_Cost

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N239

## Claim

公有云CDN请求数成本在高流量工作点（月请求量 50亿次，对应DAU 500万/日均333次请求的高频短视频场景）的量化值：Cloud_Request_Cost_High = 5,000,000,000 × ¥0.000002 (假设50亿次以上单价降至¥0.000002) = ¥10,000/月，此时请求费占比显著上升，需评估是否超过自建方案边际成本阈值。

## Corrected Claim

公有云CDN请求数成本在高流量工作点（月请求量 50亿次，对应DAU 500万/日均333次请求的高频短视频场景）的量化值：Cloud_Request_Cost_High = 5,000,000,000 × ¥0.000002 (假设50亿次以上单价降至¥0.000002) = ¥10,000/月，此时请求费占比显著上升，需评估是否超过自建方案边际成本阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：5,000,000,000 × 0.000002 = 10,000，计算无误；单价¥0.000002/次（即¥2/百万次）符合公有云CDN高流量阶梯定价的量级常识。

## Search Query

Alibaba Cloud CDN request pricing high volume tier 5 billion requests
