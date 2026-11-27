# N190: 流量分配算法随机扰动标准差 σ_Exposure 的典型值范围为 0.1-0.2，源于推荐系统中探索-利用（Explore-Exploit）机制引入的随机噪声（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

流量分配算法随机扰动标准差 σ_Exposure 的典型值范围为 0.1-0.2，源于推荐系统中探索-利用（Explore-Exploit）机制引入的随机噪声（如 Thompson Sampling 或 ε-greedy 策略的方差），该值决定了曝光量的波动幅度。

## Corrected Claim

流量分配算法随机扰动标准差 σ_Exposure 的典型值范围为 0.1-0.2，源于推荐系统中探索-利用（Explore-Exploit）机制引入的随机噪声（如 Thompson Sampling 或 ε-greedy 策略的方差），该值决定了曝光量的波动幅度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

recommender system exploration exploitation noise variance sigma typical value
