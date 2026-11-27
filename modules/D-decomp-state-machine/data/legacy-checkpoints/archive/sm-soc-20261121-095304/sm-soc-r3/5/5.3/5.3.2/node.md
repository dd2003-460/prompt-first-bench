# N166: 成交延迟成本的量化基准：高挂价导致的额外持有成本 C_delay = (P_list - P_market) * r * (T_wait_high - T_wa

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

成交延迟成本的量化基准：高挂价导致的额外持有成本 C_delay = (P_list - P_market) * r * (T_wait_high - T_wait_base)，其中 r 为资金占用利率（如年化 5%），T_wait_high/base 分别为高/正常挂价下的平均等待时间。

## Corrected Claim

成交延迟成本的量化基准：高挂价导致的额外持有成本 C_delay = (P_list - P_market) * r * (T_wait_high - T_wait_base)，其中 r 为资金占用利率（如年化 5%），T_wait_high/base 分别为高/正常挂价下的平均等待时间。

## Evidence

先验知识/题面给定，逻辑校验通过
