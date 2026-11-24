# N226: 公有云策略下回源带宽成本占比量化：基于 CHR_pub=90%（N116），回源流量占比为 10%。若阿里云边缘单价 0.18元/GB，回源单价 0.27元/G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

公有云策略下回源带宽成本占比量化：基于 CHR_pub=90%（N116），回源流量占比为 10%。若阿里云边缘单价 0.18元/GB，回源单价 0.27元/GB（1.5倍），则每 1GB 总请求中，回源成本 = 0.1GB * 0.27元/GB = 0.027元，占总带宽成本 (1GB*0.18 + 0.1GB*0.27) 的 13.1%。

## Corrected Claim

公有云策略下回源带宽成本占比量化：基于 CHR_pub=90%（N116），回源流量占比为 10%。若阿里云边缘单价 0.18元/GB，回源单价 0.27元/GB（1.5倍），则每 1GB 总请求中，回源成本 = 0.1GB * 0.27元/GB = 0.027元，占总带宽成本 (1GB*0.18 + 0.1GB*0.27) 的 13.1%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.027 / (0.18 + 0.027) ≈ 13.09%，四舍五入为 13.1%，数值与逻辑均自洽。

## Search Query

Aliyun CDN origin pull bandwidth price ratio
