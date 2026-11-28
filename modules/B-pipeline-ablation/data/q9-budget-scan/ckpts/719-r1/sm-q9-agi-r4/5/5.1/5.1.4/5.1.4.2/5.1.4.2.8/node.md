# N654: 冗余备份成本Redundancy_Cost：为应对云端故障，需保留本地20%算力冗余，其机会成本为20% × Local_Power_Cost_per_hour

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N238, N239, N240

## Claim

冗余备份成本Redundancy_Cost：为应对云端故障，需保留本地20%算力冗余，其机会成本为20% × Local_Power_Cost_per_hour × P_f_inverse，其中Local_Power_Cost_per_hour基于N340的$0.83/hour（单卡等效）计算

## Corrected Claim

冗余备份成本Redundancy_Cost：为应对云端故障，需保留本地20%算力冗余，其机会成本为20% × Local_Power_Cost_per_hour × P_f_inverse，其中Local_Power_Cost_per_hour基于N340的$0.83/hour（单卡等效）计算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

redundancy cost opportunity cost local backup infrastructure
