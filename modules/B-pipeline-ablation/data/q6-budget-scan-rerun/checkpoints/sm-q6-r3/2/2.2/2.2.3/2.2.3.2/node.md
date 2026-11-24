# N194: 公有云跨地域回源成本公式：Cost_Cross_Region_Origin = Origin_Traffic_TB × Cross_Region_Ratio ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

公有云跨地域回源成本公式：Cost_Cross_Region_Origin = Origin_Traffic_TB × Cross_Region_Ratio × Unit_Price_Cross_Region + Origin_Traffic_TB × (1 - Cross_Region_Ratio) × Unit_Price_Local，其中Unit_Price_Cross_Region通常高于Local 20%-50%（如阿里云跨域回源单价约为同域1.3-1.5倍）

## Corrected Claim

公有云跨地域回源成本公式：Cost_Cross_Region_Origin = Origin_Traffic_TB × Cross_Region_Ratio × Unit_Price_Cross_Region + Origin_Traffic_TB × (1 - Cross_Region_Ratio) × Unit_Price_Local，其中Unit_Price_Cross_Region通常高于Local 20%-50%（如阿里云跨域回源单价约为同域1.3-1.5倍）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Alibaba Cloud CDN cross-region origin pull pricing vs local pricing
