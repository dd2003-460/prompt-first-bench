# N149: C_opportunity 的量化：卖家机会成本阈值 C_opportunity 定义为卖家将商品用于其他用途（如自用、转卖其他平台或资金占用）的年化收益率 r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

C_opportunity 的量化：卖家机会成本阈值 C_opportunity 定义为卖家将商品用于其他用途（如自用、转卖其他平台或资金占用）的年化收益率 r_annual * P_high * (T_wait / 365)，若 E[Loss_high] > C_opportunity，则理性卖家应降价，反之维持高挂价。

## Corrected Claim

C_opportunity 的量化：卖家机会成本阈值 C_opportunity 定义为卖家将商品用于其他用途（如自用、转卖其他平台或资金占用）的年化收益率 r_annual * P_high * (T_wait / 365)，若 E[Loss_high] > C_opportunity，则理性卖家应降价，反之维持高挂价。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

opportunity cost threshold for holding inventory in secondary market
