# N138: r_time 的异质性参数化：买家的时间机会成本 r_time 并非固定值，而是与收入水平正相关，定义为当地平均时薪的 k 倍，其中 k ∈ [0.1, 0.3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

r_time 的异质性参数化：买家的时间机会成本 r_time 并非固定值，而是与收入水平正相关，定义为当地平均时薪的 k 倍，其中 k ∈ [0.1, 0.3]；对于高时间价值用户（如专业人士），k 取上限 0.3，对于低时间价值用户，k 取下限 0.1，这导致 C_search 在不同用户群体间存在 3 倍差异。

## Corrected Claim

r_time 的异质性参数化：买家的时间机会成本 r_time 并非固定值，而是与收入水平正相关，定义为当地平均时薪的 k 倍，其中 k ∈ [0.1, 0.3]；对于高时间价值用户（如专业人士），k 取上限 0.3，对于低时间价值用户，k 取下限 0.1，这导致 C_search 在不同用户群体间存在 3 倍差异。

## Evidence

先验知识/题面给定，逻辑校验通过：k∈[0.1, 0.3] 的上下限比值为 3，与陈述中“3 倍差异”在数学上严格自洽，且符合经济学中时间机会成本与收入正相关的常规建模逻辑。

## Search Query

time opportunity cost hourly wage multiplier consumer behavior
