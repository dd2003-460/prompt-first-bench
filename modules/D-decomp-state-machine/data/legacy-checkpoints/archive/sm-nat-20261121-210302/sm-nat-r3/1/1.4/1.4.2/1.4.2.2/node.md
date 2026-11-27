# N115: LRU 字节失效率 MissRate_LRU_byte 与 N_cap（缓存可容纳对象数）的关系：在 Pareto(β=0.9) 热度分布下，MissRate_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

LRU 字节失效率 MissRate_LRU_byte 与 N_cap（缓存可容纳对象数）的关系：在 Pareto(β=0.9) 热度分布下，MissRate_LRU_byte ≈ 1 - (N_cap / N_total)^0.9 * (S_avg_cached / S_avg_total)，其中 N_cap 由 128GB / S_avg_cached 决定，需结合 ρ=-0.3 修正 S_avg_cached。

## Corrected Claim

在 Pareto(β=0.9) 热度分布下，LRU 字节失效率 MissRate_LRU_byte 与缓存容量占比相关，通常近似为 1 - (Cache_Size / Total_Size)^β，其中 Cache_Size 和 Total_Size 均为字节数，需结合具体热度分布模型修正。

## Evidence

[质询]公式中直接混用对象数量比 (N_cap/N_total) 和字节大小比 (S_avg_cached/S_avg_total) 来估算字节失效率，且未明确 N_total 是总对象数还是总字节数，量纲和物理意义存在混淆；此外，Pareto 分布下的 LRU 失效率通常与缓存容量占总体积的比例相关，而非简单的对象数比例乘以平均大小比，该近似公式缺乏严格的理论推导支持。 | 先验知识/题面给定，但逻辑校验发现公式量纲和物理意义不自洽，且无外部来源支持该特定近似形式。
