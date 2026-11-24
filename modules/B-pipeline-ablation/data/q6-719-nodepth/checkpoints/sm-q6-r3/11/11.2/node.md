# N402: 公有云CDN请求费用占比 Cost_Ratio_Request = (Monthly_Requests × Unit_Price_Request) / (Mon

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N141

## Claim

公有云CDN请求费用占比 Cost_Ratio_Request = (Monthly_Requests × Unit_Price_Request) / (Monthly_Requests × Unit_Price_Request + Monthly_Traffic_GB × Unit_Price_Traffic_GB)，当 s_avg < 1MB 时该比例通常 > 30%，当 s_avg > 10MB 时 < 10%，需代入具体单价计算

## Corrected Claim

公有云CDN请求费用占比 Cost_Ratio_Request = (Monthly_Requests × Unit_Price_Request) / (Monthly_Requests × Unit_Price_Request + Monthly_Traffic_GB × Unit_Price_Traffic_GB)，当 s_avg < 1MB 时该比例通常 > 30%，当 s_avg > 10MB 时 < 10%，需代入具体单价计算

## Evidence

先验知识/题面给定，逻辑校验通过
