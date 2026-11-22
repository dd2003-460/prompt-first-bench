# N188: T_evict 公式的适用性边界验证：验证 N66 公式中 u * N_cap / N_total 项在 u=1%/天 时是否始终 < 0.1，若超出此范围，需

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

T_evict 公式的适用性边界验证：验证 N66 公式中 u * N_cap / N_total 项在 u=1%/天 时是否始终 < 0.1，若超出此范围，需引入非线性修正项以描述更新事件与驱逐事件的竞争机制。

## Corrected Claim

T_evict 公式中 u * N_cap / N_total 项在 u=1%/天 时的量级需根据具体 N_cap/N_total 比例计算；若该项显著影响驱逐概率（具体阈值需依据模型校准确定），则需引入非线性修正项以描述更新与驱逐的竞争机制。

## Evidence

[质询]该陈述包含具体的数值阈值（0.1）和特定的非线性修正需求，属于经验性工程参数或特定模型假设，无法从第一性原理严格推导；且缺乏来源支持该特定阈值（0.1）的普适性或正确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体阈值0.1及非线性修正的必要性）

## Search Query

LRU cache eviction period correction factor for object update rate
