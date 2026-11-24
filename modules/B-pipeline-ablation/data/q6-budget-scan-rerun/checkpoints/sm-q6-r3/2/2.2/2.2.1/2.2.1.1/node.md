# N185: 公有云 CDN 下行未命中流量的计算：Outbound_Miss_TB = Daily_Download_Traffic_TB × (1 - Cache_Hit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

公有云 CDN 下行未命中流量的计算：Outbound_Miss_TB = Daily_Download_Traffic_TB × (1 - Cache_Hit_Rate_PublicCloud)，其中 Daily_Download_Traffic_TB = 2TB，Cache_Hit_Rate_PublicCloud 通常 >95%（因节点多、缓存命中率高），故 Outbound_Miss_TB ≈ 2TB × 0.05 = 0.1TB

## Corrected Claim

公有云 CDN 下行未命中流量的计算：Outbound_Miss_TB = Daily_Download_Traffic_TB × (1 - Cache_Hit_Rate_PublicCloud)，其中 Daily_Download_Traffic_TB = 2TB，Cache_Hit_Rate_PublicCloud 通常 >95%（因节点多、缓存命中率高），故 Outbound_Miss_TB ≈ 2TB × 0.05 = 0.1TB

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义正确，数值代入（2TB * 5% = 0.1TB）计算无误，且公有云CDN高命中率（>95%）符合行业常识。
