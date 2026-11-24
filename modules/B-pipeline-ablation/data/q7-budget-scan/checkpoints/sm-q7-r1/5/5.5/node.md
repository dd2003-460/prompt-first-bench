# N30: 技术锁定风险量化：C_lock_in = (Exit_Cost_If_Switching / Expected_Useful_Life_Year)，其中 Exi

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

技术锁定风险量化：C_lock_in = (Exit_Cost_If_Switching / Expected_Useful_Life_Year)，其中 Exit_Cost 包括数据导出、API 适配、应用重构成本，对于云存储，Exit_Cost 主要由 Egress 费和代码改造工时构成，需估算从 S3 迁移到自建存储的总一次性成本。

## Corrected Claim

技术锁定风险量化：C_lock_in = (Exit_Cost_If_Switching / Expected_Useful_Life_Year)，其中 Exit_Cost 包括数据导出、API 适配、应用重构成本，对于云存储，Exit_Cost 主要由 Egress 费和代码改造工时构成，需估算从 S3 迁移到自建存储的总一次性成本。

## Evidence

先验知识/题面给定，逻辑校验通过
