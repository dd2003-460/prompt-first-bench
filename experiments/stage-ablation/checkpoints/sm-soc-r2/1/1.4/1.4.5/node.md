# N43: β_seller 的贝叶斯更新机制：β_seller_new = β_prior + η * (Success_rate_recent - Success_ra

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

β_seller 的贝叶斯更新机制：β_seller_new = β_prior + η * (Success_rate_recent - Success_rate_prior)，其中 η 为学习率（0.1-0.3），Success_rate 定义为过去30天成交溢价率 > 10% 的比例，该机制导致 β_seller 在卖家间呈现动态收敛而非静态分布。

## Corrected Claim

β_seller 的贝叶斯更新机制：β_seller_new = β_prior + η * (Success_rate_recent - Success_rate_prior)，其中 η 为学习率（0.1-0.3），Success_rate 定义为过去30天成交溢价率 > 10% 的比例，该机制导致 β_seller 在卖家间呈现动态收敛而非静态分布。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller pricing strategy bayesian update learning rate
