# N293: Hardware_Failure_Cost = (Annual_Failure_Rate × 10_Pops) × (MTTR_Hours × Hourly_O

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

Hardware_Failure_Cost = (Annual_Failure_Rate × 10_Pops) × (MTTR_Hours × Hourly_Ops_Cost + Spare_Part_Replacement_Cost)，其中 Annual_Failure_Rate 典型值为 5%-10%（服务器/存储），MTTR 受备件库存影响，若无本地备件 MTTR 可达 24h，有备件则 4h。

## Corrected Claim

Hardware_Failure_Cost = (Annual_Failure_Rate × 10_Pops) × (MTTR_Hours × Hourly_Ops_Cost + Spare_Part_Replacement_Cost)，其中 Annual_Failure_Rate 典型值为 5%-10%（服务器/存储），MTTR 受备件库存影响，若无本地备件 MTTR 可达 24h，有备件则 4h。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

data center hardware failure rate MTTR impact on ops cost
