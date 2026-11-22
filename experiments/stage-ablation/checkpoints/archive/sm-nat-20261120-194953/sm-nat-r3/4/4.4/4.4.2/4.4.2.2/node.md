# N134: 量化 N60 中 '主要由冷对象失效主导' 的边界条件：当且仅当缓存容量 K_cap < 10^5（即非全量驻留）且冷对象平均驻留时间 T_cold > 1/u

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

量化 N60 中 '主要由冷对象失效主导' 的边界条件：当且仅当缓存容量 K_cap < 10^5（即非全量驻留）且冷对象平均驻留时间 T_cold > 1/u 时，冷对象失效项 P_inval_cold * W_cold 才可能超过热门对象项；在本题 K_cap >> 10^5 条件下，该前提不成立，N60 的权重分配错误。

## Corrected Claim

量化 N60 中 '主要由冷对象失效主导' 的边界条件：当且仅当缓存容量 K_cap < 10^5（即非全量驻留）且冷对象平均驻留时间 T_cold > 1/u 时，冷对象失效项 P_inval_cold * W_cold 才可能超过热门对象项；在本题 K_cap >> 10^5 条件下，该前提不成立，N60 的权重分配错误。

## Evidence

先验知识/题面给定，逻辑校验通过
