# N124: 基准成交量 Q_base 在干预前的估计值需基于卖家历史成交率计算，假设 Q_base = N_listings * P_deal_base，其中 P_deal

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

基准成交量 Q_base 在干预前的估计值需基于卖家历史成交率计算，假设 Q_base = N_listings * P_deal_base，其中 P_deal_base 为基准挂价下的成交概率，需排除季节性波动影响，取过去90天均值

## Corrected Claim

基准成交量 Q_base 在干预前的估计值需基于卖家历史成交率计算，假设 Q_base = N_listings * P_deal_base，其中 P_deal_base 为基准挂价下的成交概率，需排除季节性波动影响，取过去90天均值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

baseline transaction rate calculation for second hand sellers
