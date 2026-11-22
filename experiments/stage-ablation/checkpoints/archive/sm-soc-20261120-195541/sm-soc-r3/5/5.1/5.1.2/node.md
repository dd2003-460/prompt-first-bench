# N164: 点击-成交转化率（CVR）的筛选效应量化：CVR_high = N_deals_high / N_clicks_high，CVR_low = N_deals_l

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

点击-成交转化率（CVR）的筛选效应量化：CVR_high = N_deals_high / N_clicks_high，CVR_low = N_deals_low / N_clicks_low，筛选效应存在当且仅当 CVR_high - CVR_low > 0.10 * CVR_low，且 t 检验 p < 0.05；假设 CVR_low=5.0%，则 CVR_high 需 > 5.5%。

## Corrected Claim

点击-成交转化率（CVR）的筛选效应量化：CVR_high = N_deals_high / N_clicks_high，CVR_low = N_deals_low / N_clicks_low，筛选效应存在当且仅当 CVR_high - CVR_low > 0.10 * CVR_low，且 t 检验 p < 0.05；假设 CVR_low=5.0%，则 CVR_high 需 > 5.5%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 5.0% * (1 + 0.10) = 5.5% 正确，统计检验逻辑自洽。

## Search Query

conversion rate difference test for funnel analysis
