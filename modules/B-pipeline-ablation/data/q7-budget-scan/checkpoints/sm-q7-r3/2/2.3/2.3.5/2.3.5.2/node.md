# N217: Intelligent-Tiering 层级转换成本：数据在 Frequent Access 与 Infrequent Access 层级间转换时，无额外转换费

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

Intelligent-Tiering 层级转换成本：数据在 Frequent Access 与 Infrequent Access 层级间转换时，无额外转换费，但层级判定基于 30 天访问统计；若数据访问模式波动（如季节性），可能导致频繁层级切换，增加监控复杂度，但无直接财务成本，仅影响运维人力 ~0.1 人时/年，折算 ~¥1,000/年。

## Corrected Claim

Intelligent-Tiering 层级转换无额外转换费，层级判定基于 30 天访问统计；若数据访问模式波动，可能导致频繁层级切换，增加监控复杂度，但无直接财务成本，仅产生少量运维人力开销（具体数值视监控体系而定）。

## Evidence

[质询]「~0.1 人时/年」及「~¥1,000/年」的运维成本估算属于高度依赖具体业务场景、监控工具成熟度及人力单价的经验性假设，缺乏通用标准或第一性原理支持，且未提供计算依据，存在数值量级随意性风险。 | 先验知识/题面给定，逻辑校验通过：AWS Intelligent-Tiering 确实无层级转换费，基于30天统计，逻辑自洽；但具体运维成本数值为经验估算，无来源支持，故降级。
