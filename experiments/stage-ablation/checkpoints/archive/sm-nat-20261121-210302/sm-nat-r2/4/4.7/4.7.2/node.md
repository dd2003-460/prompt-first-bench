# N64: 对象更新率 u=1%/天 对 LFU 的惩罚项：Stale_Penalty = 1 - (1 - u)^{T_resident_LFU}，其中 T_reside

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

对象更新率 u=1%/天 对 LFU 的惩罚项：Stale_Penalty = 1 - (1 - u)^{T_resident_LFU}，其中 T_resident_LFU 是 LFU 中对象的平均驻留时间，需结合访问频率分布计算

## Corrected Claim

对象更新率 u=1%/天 对 LFU 的惩罚项：Stale_Penalty = 1 - (1 - u)^{T_resident_LFU}，其中 T_resident_LFU 是 LFU 中对象的平均驻留时间，需结合访问频率分布计算

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Stale_Penalty = 1 - (1 - u)^T 符合指数衰减/更新概率模型的基本逻辑，量纲与数值范围合理（0到1之间），且 source 为 knowledge，无需外部来源支持。
