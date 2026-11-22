# N133: 感知阈值方差参数化：σ_pct = c * (1 + 1/n_reviews)，其中 c 为基准方差常数（约 2%），n_reviews 为该商品的历史评价数，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

感知阈值方差参数化：σ_pct = c * (1 + 1/n_reviews)，其中 c 为基准方差常数（约 2%），n_reviews 为该商品的历史评价数，评价数越少买家不确定性越高，感知阈值波动越大，导致 P_no_inquiry 的置信区间变宽。

## Corrected Claim

感知阈值方差参数化：σ_pct = c * (1 + 1/n_reviews)，其中 c 为基准方差常数（约 2%），n_reviews 为该商品的历史评价数，评价数越少买家不确定性越高，感知阈值波动越大，导致 P_no_inquiry 的置信区间变宽。

## Evidence

先验知识/题面给定，逻辑校验通过：该参数化形式符合贝叶斯统计中先验方差随样本量增加而收敛的直觉（评价数越少，不确定性越高，方差越大），量纲与逻辑自洽。

## Search Query

uncertainty variance product reviews price perception
