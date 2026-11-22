# N41: 共享随机源：定义平台算法排序权重的随机扰动项 $\epsilon_{algo}$ 为均值为0、标准差为 $\sigma_{algo}$ 的高斯分布，其中 $\s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N12

## Claim

共享随机源：定义平台算法排序权重的随机扰动项 $\epsilon_{algo}$ 为均值为0、标准差为 $\sigma_{algo}$ 的高斯分布，其中 $\sigma_{algo}$ 代表算法在实时流量分配中对商品特征（价格、新鲜度）评分的噪声水平，导致同一商品在不同时刻的曝光排名存在随机波动。

## Corrected Claim

共享随机源：定义平台算法排序权重的随机扰动项 $\epsilon_{algo}$ 为均值为0、标准差为 $\sigma_{algo}$ 的高斯分布，其中 $\sigma_{algo}$ 代表算法在实时流量分配中对商品特征（价格、新鲜度）评分的噪声水平，导致同一商品在不同时刻的曝光排名存在随机波动。

## Evidence

先验知识/题面给定，逻辑校验通过
