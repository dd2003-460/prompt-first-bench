# N265: 买家价格接受阈值分布 σ_buyer 的量化：σ_buyer = (P_ask_max - V) / V，其中 P_ask_max 为买家愿意接受的最高挂价，该

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

买家价格接受阈值分布 σ_buyer 的量化：σ_buyer = (P_ask_max - V) / V，其中 P_ask_max 为买家愿意接受的最高挂价，该参数决定了 exp 函数中 (P_ask - V) 的有效作用范围，需通过买家出价数据回归得出。

## Corrected Claim

买家价格接受阈值分布 σ_buyer 的量化：σ_buyer = (P_ask_max - V) / V，其中 P_ask_max 为买家愿意接受的最高挂价，该参数决定了 exp 函数中 (P_ask - V) 的有效作用范围，需通过买家出价数据回归得出。

## Evidence

先验知识/题面给定，逻辑校验通过
