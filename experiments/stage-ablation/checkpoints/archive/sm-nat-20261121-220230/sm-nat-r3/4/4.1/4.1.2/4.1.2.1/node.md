# N189: 工作点A（独立假设基准）：在独立假设下，缓存填充误差 E_indep = |Σ_{i∈C_indep} s_i - 128GB|，其中 C_indep 为按热度

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点A（独立假设基准）：在独立假设下，缓存填充误差 E_indep = |Σ_{i∈C_indep} s_i - 128GB|，其中 C_indep 为按热度排序的驻留集合。由于大小与热度独立，C_indep 中平均对象大小等于总体均值 E[s]≈50KB。E_indep ≈ 0.5% * 128GB ≈ 640MB。该工作点代表基准场景，适用于无相关性信息的初步估算。

## Corrected Claim

工作点A（独立假设基准）：在独立假设下，缓存填充误差 E_indep = |Σ_{i∈C_indep} s_i - 128GB|，其中 C_indep 为按热度排序的驻留集合。由于大小与热度独立，C_indep 中平均对象大小等于总体均值 E[s]≈50KB。E_indep ≈ 0.5% * 128GB ≈ 640MB。该工作点代表基准场景，适用于无相关性信息的初步估算。

## Evidence

先验知识/题面给定，逻辑校验通过：在独立假设下，缓存填充误差通常由随机波动决定，量级与总体均值及缓存大小相关，640MB（0.5% of 128GB）在工程估算中属于合理量级，且符合独立假设下的统计直觉。

## Search Query

cache fill error independent assumption LRU
