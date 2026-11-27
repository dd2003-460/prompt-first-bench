# N37: 市场公允价格 P_market 的代理变量计算公式：P_market = (P_median_recent * w_median + P_mean_volume

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

市场公允价格 P_market 的代理变量计算公式：P_market = (P_median_recent * w_median + P_mean_volume * w_mean) / (w_median + w_mean)，其中 w_median 和 w_mean 为权重，需根据商品类别（如电子产品 vs 奢侈品）进行差异化设定。

## Corrected Claim

市场公允价格 P_market 的代理变量计算公式：P_market = (P_median_recent * w_median + P_mean_volume * w_mean) / (w_median + w_mean)，其中 w_median 和 w_mean 为权重，需根据商品类别（如电子产品 vs 奢侈品）进行差异化设定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

market fair price proxy median recent sales volume weighted average
