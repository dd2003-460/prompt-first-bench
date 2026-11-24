# N702: Unit_Price_Origin_Fetch_GB 的构成：Unit_Price_Origin_Fetch_GB = Price_Origin_Bandwid

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N242

## Claim

Unit_Price_Origin_Fetch_GB 的构成：Unit_Price_Origin_Fetch_GB = Price_Origin_Bandwidth_GB + Price_Origin_Compute_GB，其中 Price_Origin_Bandwidth_GB 为源站出口带宽成本分摊（约 ¥0.1-0.3/GB，取决于源站带宽利用率），Price_Origin_Compute_GB 为源站 CPU/IO 处理成本分摊（约 ¥0.01-0.05/GB）。合计典型值为 ¥0.15-0.35/GB，低于公有云 CDN 回源流量费（¥0.2-0.5/GB）。

## Corrected Claim

Unit_Price_Origin_Fetch_GB 的构成：Unit_Price_Origin_Fetch_GB = Price_Origin_Bandwidth_GB + Price_Origin_Compute_GB，其中 Price_Origin_Bandwidth_GB 为源站出口带宽成本分摊（约 ¥0.1-0.3/GB，取决于源站带宽利用率），Price_Origin_Compute_GB 为源站 CPU/IO 处理成本分摊（约 ¥0.01-0.05/GB）。合计典型值为 ¥0.15-0.35/GB，低于公有云 CDN 回源流量费（¥0.2-0.5/GB）。

## Evidence

先验知识/题面给定，逻辑校验通过
