# N267: 平均成交时长 T_avg 的量化影响：T_avg = ΣT_i / N_sold，其中 T_i 为第 i 件商品成交时长；T_avg < 7 天时，买家搜索时间

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N85, N86, N87

## Claim

平均成交时长 T_avg 的量化影响：T_avg = ΣT_i / N_sold，其中 T_i 为第 i 件商品成交时长；T_avg < 7 天时，买家搜索时间减少比例额外增加 3-8%，需验证该阈值

## Corrected Claim

平均成交时长 T_avg 的量化影响：T_avg = ΣT_i / N_sold，其中 T_i 为第 i 件商品成交时长；存在一个阈值（如 T_avg < 7 天），当低于该阈值时，买家搜索时间减少比例可能额外增加（具体比例需进一步验证，原称 3-8%）。

## Evidence

[质询]该陈述包含具体的经验性阈值（T_avg < 7天）及具体的量化影响范围（3-8%），属于经验事实而非第一性原理可推导的数学或逻辑结论。在缺乏外部来源支持的情况下，无法验证该特定阈值和百分比的准确性，存在数值量级或具体参数错误的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值阈值无法从第一性原理严格推出）

## Search Query

average time to sell impact on buyer search efficiency threshold 7 days
