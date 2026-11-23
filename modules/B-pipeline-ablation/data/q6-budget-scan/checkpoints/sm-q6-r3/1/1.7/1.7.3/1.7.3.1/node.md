# N229: SLA_self 的量化计算式：SLA_self = 1 - (MTTR * MTBF_factor) / Total_Time，其中 MTTR (Mean T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

SLA_self 的量化计算式：SLA_self = 1 - (MTTR * MTBF_factor) / Total_Time，其中 MTTR (Mean Time To Repair) 典型值为 5-30 分钟（取决于自动化运维水平），Total_Time 为月度总秒数（2,592,000s），需结合故障频率估算得出具体 SLA 值（如 99.9% 或 99.95%）

## Corrected Claim

SLA_self 的量化计算式：SLA_self = 1 - (MTTR * MTBF_factor) / Total_Time，其中 MTTR (Mean Time To Repair) 典型值为 5-30 分钟（取决于自动化运维水平），Total_Time 为月度总秒数（2,592,000s），需结合故障频率估算得出具体 SLA 值（如 99.9% 或 99.95%）

## Evidence

先验知识/题面给定，逻辑校验通过：SLA公式结构符合可靠性工程定义，MTTR典型值（5-30分钟）及月度总秒数（2,592,000s）量级合理，无内部矛盾。

## Search Query

CDN node MTTR typical value minutes SRE
