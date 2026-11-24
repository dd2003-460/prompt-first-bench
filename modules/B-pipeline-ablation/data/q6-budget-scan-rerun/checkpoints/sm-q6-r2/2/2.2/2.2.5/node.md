# N64: 自建POP策略下，Inbound_Traffic_TB 的带宽预留成本计算：需预留的入向带宽 = (Daily_Upload_Traffic_TB (0.2TB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

自建POP策略下，Inbound_Traffic_TB 的带宽预留成本计算：需预留的入向带宽 = (Daily_Upload_Traffic_TB (0.2TB) + Daily_Download_Miss_Traffic_TB) / 86400s * 8 * 1024^2，通常入向带宽需求仅为出向的10%-20%，成本占比低

## Corrected Claim

自建POP策略下，Inbound_Traffic_TB 的带宽预留成本计算：需预留的入向带宽 = (Daily_Upload_Traffic_TB (0.2TB) + Daily_Download_Miss_Traffic_TB) / 86400s * 8 * 1024^2，通常入向带宽需求仅为出向的10%-20%，成本占比低

## Evidence

先验知识/题面给定，逻辑校验通过：带宽计算公式量纲正确（TB/s * 8 * 1024^2 转换为 Mbps 或 Gbps 取决于单位定义，此处逻辑自洽），且入向带宽通常低于出向带宽符合CDN/POP网络流量特征（缓存命中导致出向大，入向仅回源或上传小）。
