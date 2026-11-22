# N79: LRU 稳态字节命中率下界的精确数值推导：在 N_cache 覆盖全部对象的前提下，LRU 的字节命中率 H_byte_LRU 由未缓存对象的字节占比决定，但由

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N26

## Claim

LRU 稳态字节命中率下界的精确数值推导：在 N_cache 覆盖全部对象的前提下，LRU 的字节命中率 H_byte_LRU 由未缓存对象的字节占比决定，但由于 N_cache > 100,000，所有对象均在缓存中，因此 H_byte_LRU_base = 1.0；考虑更新失效后，有效命中率 H_eff = 1.0 * D_update，其中 D_update 由 N33 给出，若平均驻留时间 T_residence_avg = 1 小时，则 H_eff ≈ 0.9996，即 99.96%。

## Corrected Claim

在假设 N_cache 覆盖全部对象且平均驻留时间为 1 小时、更新失效因子 D_update 由 N33 给定的前提下，LRU 的有效字节命中率 H_eff 约为 99.96%。

## Evidence

父节点级核验未通过：非正交（子节点2与父节点及子节点1存在数值和逻辑上的矛盾。父节点设定 T_res=1h 得出 H_eff=99.96%，而子节点2重新推导 T_res=20s 得出 H_eff=99.9998%，两者结论冲突。此外，子节点2引入的新参数（λ_cold, Pareto估计）未在父节点中定义，导致分解后的信息流不连贯，且子节点1仅陈述了子节点2前提下的特例，缺乏独立性。）

## Search Query

LRU cache hit rate steady state calculation 100000 objects 128GB memory Pareto distribution update rate 1% per day
