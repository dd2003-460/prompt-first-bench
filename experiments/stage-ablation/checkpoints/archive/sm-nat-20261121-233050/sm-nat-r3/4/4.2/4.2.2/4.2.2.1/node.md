# N121: 在 M/C=1.0 的边界条件下，P_invalid=0 的结论依赖于 T_LRU_avg → ∞ 的假设。若考虑对象大小分布的离散性，实际 T_res_min

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

在 M/C=1.0 的边界条件下，P_invalid=0 的结论依赖于 T_LRU_avg → ∞ 的假设。若考虑对象大小分布的离散性，实际 T_res_min = (Cache_Size / Max_Object_Size) / (Max_Frequency * Max_Object_Size)，对于最大对象（100MB）和最高频对象（10000次/天），T_res_min ≈ (131072MB / 100MB) / (10000 * 100MB) 天，需计算最小驻留时间下的 P_invalid_max = 1 - exp(-0.01 * T_res_min)。

## Corrected Claim

在 M/C=1.0 边界条件下，若考虑对象大小分布，最小驻留时间 T_res_min 主要由最高访问频率决定（T_res_min ≈ 1 / Max_Frequency），而非与对象大小成反比。原公式量纲错误，需修正为基于频率的时间尺度计算 P_invalid。

## Evidence

[质询]公式量纲错误：T_res_min 的计算公式中分母包含 Max_Object_Size，导致量纲为 1/(Frequency * Size)，而非时间单位（天）。正确的最小驻留时间应仅取决于访问频率（T_res_min ≈ 1 / Max_Frequency），与对象大小无关（假设缓存容量足够容纳该对象）。此外，P_invalid 的指数项系数 0.01 缺乏定义和来源支持。 | 逻辑校验发现量纲矛盾：(Cache_Size / Max_Object_Size) 无量纲，除以 (Max_Frequency * Max_Object_Size) 后单位不为时间。经验事实且无来源支持，公式推导存在硬逻辑错误。

## Search Query

LRU cache residency time calculation for large objects with high frequency
