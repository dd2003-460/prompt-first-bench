# N266: 历史降价频率 F_decrease 的量化影响：F_decrease = N_decrease / N_total，其中 N_decrease 为过去 90 天

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N85, N86, N87

## Claim

历史降价频率 F_decrease 的量化影响：F_decrease = N_decrease / N_total，其中 N_decrease 为过去 90 天降价次数，N_total 为总挂牌次数；F_decrease > 0.3 时，买家搜索时间减少比例额外增加 5-10%，需验证该阈值

## Corrected Claim

历史降价频率 F_decrease 的量化影响：F_decrease = N_decrease / N_total，其中 N_decrease 为过去 90 天降价次数，N_total 为总挂牌次数；较高的 F_decrease 通常与买家决策时间的缩短相关，具体阈值（如 0.3）及影响幅度（如 5-10%）需通过实证数据验证。

## Evidence

[质询]该陈述包含具体的经验性阈值（F_decrease > 0.3）和具体的量化影响（搜索时间减少比例额外增加 5-10%），这属于市场行为统计规律，无法从第一性原理或数学公理中严格推导出来，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该具体数值阈值非第一性原理可推导内容）

## Search Query

frequency of price reduction impact on buyer search time threshold 0.3
