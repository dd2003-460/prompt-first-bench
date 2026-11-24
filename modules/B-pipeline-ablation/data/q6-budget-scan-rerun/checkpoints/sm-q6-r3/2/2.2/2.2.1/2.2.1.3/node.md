# N188: 公有云 CDN 下行未命中流量对每千请求成本的贡献：Cost_Outbound_per_1k_Req = (Outbound_Miss_TB × 1024 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

公有云 CDN 下行未命中流量对每千请求成本的贡献：Cost_Outbound_per_1k_Req = (Outbound_Miss_TB × 1024 GB/TB × Unit_Price_¥/GB) / (Total_Daily_Requests / 1000)，其中 Unit_Price_¥/GB 为阿里云 CDN 按流量计价的单价（如 ¥0.24/GB）

## Corrected Claim

公有云 CDN 下行未命中流量对每千请求成本的贡献：Cost_Outbound_per_1k_Req = (Outbound_Miss_TB × 1024 GB/TB × Unit_Price_¥/GB) / (Total_Daily_Requests / 1000)，其中 Unit_Price_¥/GB 为阿里云 CDN 按流量计价的单价（如 ¥0.24/GB）

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（TB转GB，总价除以千次请求数），阿里云CDN下行流量单价¥0.24/GB符合市场常识量级。
