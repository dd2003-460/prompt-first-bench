# N85: 均衡移动幅度 ΔEquilibrium 的量化：ΔEquilibrium = |P_market_post - P_market_pre| / P_market

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

均衡移动幅度 ΔEquilibrium 的量化：ΔEquilibrium = |P_market_post - P_market_pre| / P_market_pre，其中 P_market_pre 和 P_market_post 分别为干预前后同类商品的成交均价，若 ΔEquilibrium < 5%，则表明干预未有效打破原有均衡，策略有效性置信度低。

## Corrected Claim

均衡移动幅度 ΔEquilibrium 的量化：ΔEquilibrium = |P_market_post - P_market_pre| / P_market_pre，其中 P_market_pre 和 P_market_post 分别为干预前后同类商品的成交均价，若 ΔEquilibrium < 5%，则表明干预未有效打破原有均衡，策略有效性置信度低。

## Evidence

先验知识/题面给定，逻辑校验通过
