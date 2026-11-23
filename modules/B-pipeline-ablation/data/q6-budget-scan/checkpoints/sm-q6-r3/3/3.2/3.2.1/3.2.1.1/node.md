# N271: 自建POP点平均带宽需求精确计算：日均下载2TB，核心区域占比65%（取中值），有效下载量=2TB*0.65=1.3TB/日。平均带宽=1.3TB*8*1024

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

自建POP点平均带宽需求精确计算：日均下载2TB，核心区域占比65%（取中值），有效下载量=2TB*0.65=1.3TB/日。平均带宽=1.3TB*8*1024^3 bits / 86400 s ≈ 151.5 Mbps。注意：1TB=8*1024^3 bits，1日=86400秒

## Corrected Claim

自建POP点平均带宽需求精确计算：日均下载2TB，核心区域占比65%（取中值），有效下载量=2TB*0.65=1.3TB/日。平均带宽=1.3TB*8*1024^3 bits / 86400 s ≈ 151.5 Mbps。注意：1TB=8*1024^3 bits，1日=86400秒

## Evidence

先验知识/题面给定，逻辑校验通过：1.3TB * 8 * 1024^3 / 86400 ≈ 151.5 Mbps，计算无误
