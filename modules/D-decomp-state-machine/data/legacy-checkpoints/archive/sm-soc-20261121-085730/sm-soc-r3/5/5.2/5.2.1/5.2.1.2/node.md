# N320: 逐利行为强度指数 I_profit 的量化定义与计算窗口：I_profit = (N_price_cuts_7d / N_listings) / (N_pric

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N112, N113

## Claim

逐利行为强度指数 I_profit 的量化定义与计算窗口：I_profit = (N_price_cuts_7d / N_listings) / (N_price_cuts_avg_30d / N_listings_avg)，其中 N_price_cuts_7d 为过去7天降价次数，N_price_cuts_avg_30d 为过去30天日均降价次数，该指数用于标准化不同卖家间的逐利程度差异。

## Corrected Claim

逐利行为强度指数 I_profit 的量化定义与计算窗口：I_profit = (N_price_cuts_7d / N_listings) / (N_price_cuts_avg_30d / N_listings_avg)，其中 N_price_cuts_7d 为过去7天降价次数，N_price_cuts_avg_30d 为过去30天日均降价次数，该指数用于标准化不同卖家间的逐利程度差异。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller price cutting frequency index definition short term vs long term baseline
