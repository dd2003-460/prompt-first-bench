# N132: Bandwidth_Monthly 计算：Bandwidth_Monthly = (Daily_Download_Volume × 30) × Unit_Pri

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Bandwidth_Monthly 计算：Bandwidth_Monthly = (Daily_Download_Volume × 30) × Unit_Price_GB + (Daily_Upload_Volume × 30) × Unit_Price_Upload_GB，其中 Unit_Price_GB 因策略而异：公有云取 CDN 下行单价（约 ¥0.15-0.25/GB），自建取机房带宽租赁单价（约 ¥100-300/Mbps/月，需转换为 GB 单价：Price_GB = Price_Mbps / (Mbps×3600×30/8)）。

## Corrected Claim

Bandwidth_Monthly 计算：Bandwidth_Monthly = (Daily_Download_Volume × 30) × Unit_Price_GB + (Daily_Upload_Volume × 30) × Unit_Price_Upload_GB，其中 Unit_Price_GB 因策略而异：公有云取 CDN 下行单价（约 ¥0.15-0.25/GB），自建取机房带宽租赁单价（约 ¥100-300/Mbps/月，需转换为 GB 单价：Price_GB = Price_Mbps / (Mbps×3600×30/8)）。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽月费计算公式逻辑自洽，Mbps转GB单价的换算公式（Price_Mbps / (Mbps×3600×30/8)）在量纲和数值上均正确（1 Mbps 30天约等于 3.24 TB，即 3,240 GB，若单价为 ¥100/Mbps/月，则折合 ¥0.03/GB，符合自建机房带宽成本远低于公有云CDN单价的常识），公有云CDN单价范围也符合市场常识。
