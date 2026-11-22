# N228: 搜索阈值 T_search 对成交概率 Q 的截断效应：计算 P(P_ask > T_search) 的概率质量，若 P_ask 高于 T_search 则 Q

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

搜索阈值 T_search 对成交概率 Q 的截断效应：计算 P(P_ask > T_search) 的概率质量，若 P_ask 高于 T_search 则 Q=0，否则 Q=Q_base * exp(-α*(P_ask-P_market))，需量化 T_search 相对于 P_market 的偏移量（如 5%）及其对 Q 的边际影响。

## Corrected Claim

搜索阈值 T_search 对成交概率 Q 的截断效应：计算 P(P_ask > T_search) 的概率质量，若 P_ask 高于 T_search 则 Q=0，否则 Q=Q_base * exp(-α*(P_ask-P_market))，需量化 T_search 相对于 P_market 的偏移量（如 5%）及其对 Q 的边际影响。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

search threshold price cutoff effect on conversion rate e-commerce
