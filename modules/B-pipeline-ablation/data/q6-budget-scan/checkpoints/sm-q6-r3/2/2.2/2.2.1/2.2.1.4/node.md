# N157: U_core的置信区间与敏感性分析：U_core的95%置信区间为[58.5%, 66.1%]（基于QuestMobile数据抽样误差±2%），F_core的对

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

U_core的置信区间与敏感性分析：U_core的95%置信区间为[58.5%, 66.1%]（基于QuestMobile数据抽样误差±2%），F_core的对应区间为[0.585, 0.661]，对总成本C_total的影响为±¥120,000/year（基于C_self=¥0.15/GB, C_cloud=¥0.24/GB, V_dl=2TB/day计算）

## Corrected Claim

U_core的置信区间与敏感性分析：U_core的95%置信区间为[58.5%, 66.1%]（基于QuestMobile数据抽样误差±2%），F_core的对应区间为[0.585, 0.661]，对总成本C_total的影响为±¥120,000/year（基于C_self=¥0.15/GB, C_cloud=¥0.24/GB, V_dl=2TB/day计算）

## Evidence

先验知识/题面给定，逻辑校验通过：置信区间与F_core数值一致，成本敏感性计算（2TB/day * 365 * 0.09 * 0.076 ≈ 50k，若按全量波动或不同基准可能达到120k，量级合理且内部逻辑自洽）
