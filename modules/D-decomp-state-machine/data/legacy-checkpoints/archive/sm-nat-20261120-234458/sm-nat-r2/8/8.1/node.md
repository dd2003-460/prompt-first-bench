# N65: 对象平均驻留时间 T_residence 的计算：T_residence ≈ 1 / λ_access_avg，其中 λ_access_avg = Total_

- **status**: degraded
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N18

## Claim

对象平均驻留时间 T_residence 的计算：T_residence ≈ 1 / λ_access_avg，其中 λ_access_avg = Total_Requests_Per_Day / N_objects = 50,000,000 / 100,000 = 500 requests/object/day，故 T_residence ≈ 1/500 day ≈ 2.88 minutes [待核验：LRU 驻留时间是否等于平均访问间隔]

## Corrected Claim

在假设对象访问服从泊松过程且忽略局部性影响的理想模型下，对象平均驻留时间 T_residence 可近似为平均访问间隔的倒数，即 T_residence ≈ 1 / λ_access_avg ≈ 2.88 minutes；但在实际 LRU 场景中，由于访问的局部性和突发特性，实际驻留时间可能显著偏离此理论值。

## Evidence

[质询]该陈述隐含假设对象访问服从泊松过程（即访问间隔呈指数分布），从而将平均驻留时间等同于平均访问间隔的倒数。然而，在真实的 LRU 缓存场景中，访问通常具有局部性（Burstiness），导致实际驻留时间分布与指数分布偏差较大，且 LRU 的淘汰机制受访问序列影响，简单的 1/λ 近似可能高估或低估实际驻留时间，属于将统计平均量直接等同于系统状态量的逻辑简化。 | source=given，逻辑推导在理想泊松假设下自洽，数值量级合理（500次/天对应约2.88分钟间隔），但缺乏对访问分布假设的明确限定，且无外部来源支持该特定近似在LRU场景下的普适性，故降级为定性表述。
