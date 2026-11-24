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

父节点级核验未通过：不完备（子节点涵盖了代码改造、数据校验、过渡期双跑及人员培训四个维度，彼此独立且无重叠（正交性好）。然而，父节点明确定义 Exit_Cost 包含 'Egress 费'（数据流出带宽费用），这是云存储迁移中通常占比极大的一项成本，但在四个子节点中均未体现，导致关键成本项缺失（不完备）。此外，各子节点代表不同的成本类别，并非同一参数的不同取值，因此不存在冗余。）
