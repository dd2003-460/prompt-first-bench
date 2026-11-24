# N30: 技术锁定风险量化：C_lock_in = (Exit_Cost_If_Switching / Expected_Useful_Life_Year)，其中 Exi

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

技术锁定风险量化：C_lock_in = (Exit_Cost_If_Switching / Expected_Useful_Life_Year)，其中 Exit_Cost 包括数据导出、API 适配、应用重构成本，对于云存储，Exit_Cost 主要由 Egress 费和代码改造工时构成，需估算从 S3 迁移到自建存储的总一次性成本。

## Corrected Claim

技术锁定风险量化：C_lock_in = (Exit_Cost_If_Switching / Expected_Useful_Life_Year)，其中 Exit_Cost 包括数据导出、API 适配、应用重构成本，对于云存储，Exit_Cost 主要由 Egress 费和代码改造工时构成，需估算从 S3 迁移到自建存储的总一次性成本。

## Evidence

父节点级核验未通过：不完备（子节点在维度上基本正交（代码改造、数据校验、过渡期运维、人员培训），无重叠或矛盾。但存在重大缺失：父节点明确指出云存储迁移的主要成本是'Egress费'（数据出站流量费），而4个子节点中均未包含此项关键成本，导致对C_lock_in的量化不完整。此外，'双跑成本'和'学习培训'属于过渡期一次性支出，与'Exit_Cost'定义相符，但缺少核心的数据传输成本。）
