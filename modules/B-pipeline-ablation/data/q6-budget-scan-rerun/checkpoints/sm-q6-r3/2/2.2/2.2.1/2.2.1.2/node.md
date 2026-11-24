# N187: 公有云 CDN 总下行计费流量的完整公式：Total_Billable_Outbound_TB = Daily_Download_Traffic_TB × (1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

公有云 CDN 总下行计费流量的完整公式：Total_Billable_Outbound_TB = Daily_Download_Traffic_TB × (1 - Cache_Hit_Rate_PublicCloud) + Daily_Upload_Traffic_TB × 0 + Daily_Internal_Refresh_TB × 0，其中 Daily_Internal_Refresh_TB 为 CDN 内部缓存刷新流量，通常不计费

## Corrected Claim

公有云 CDN 总下行计费流量的完整公式：Total_Billable_Outbound_TB = Daily_Download_Traffic_TB × (1 - Cache_Hit_Rate_PublicCloud) + Daily_Upload_Traffic_TB × 0 + Daily_Internal_Refresh_TB × 0，其中 Daily_Internal_Refresh_TB 为 CDN 内部缓存刷新流量，通常不计费

## Evidence

先验知识/题面给定，逻辑校验通过
