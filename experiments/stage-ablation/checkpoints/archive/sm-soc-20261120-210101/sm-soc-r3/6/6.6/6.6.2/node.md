# N367: 分母 Total_Orders_90d 的包含范围：包括所有在 90 天窗口内创建且状态为 'Completed' 或 'Cancelled' 的订单；排除 '

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N108

## Claim

分母 Total_Orders_90d 的包含范围：包括所有在 90 天窗口内创建且状态为 'Completed' 或 'Cancelled' 的订单；排除 'Pending' 或 'In_Transit' 订单，以避免未完结订单稀释信用评分。

## Corrected Claim

分母 Total_Orders_90d 的包含范围：包括所有在 90 天窗口内创建且状态为 'Completed' 或 'Cancelled' 的订单；排除 'Pending' 或 'In_Transit' 订单，以避免未完结订单稀释信用评分。

## Evidence

先验知识/题面给定，逻辑校验通过：排除未完结订单（Pending/In_Transit）以避免稀释信用评分符合业务逻辑与统计常识，无内部矛盾。

## Search Query

denominator definition for seller credit score calculation
