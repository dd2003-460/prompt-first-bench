# N314: K_noise 共享随机源定义：K_noise(t) ~ N(1, σ_noise²)，其中 σ_noise = 0.075（取5%-10%区间中值），且 K_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N103

## Claim

K_noise 共享随机源定义：K_noise(t) ~ N(1, σ_noise²)，其中 σ_noise = 0.075（取5%-10%区间中值），且 K_noise(t) 与 K_periodic(t) 及 K_event(t) 统计独立；该噪声是扣除周期与事件后的残差项，驱动缓存命中率的高频抖动。

## Corrected Claim

K_noise 共享随机源定义：K_noise(t) ~ N(1, σ_noise²)，其中 σ_noise = 0.075（取5%-10%区间中值），且 K_noise(t) 与 K_periodic(t) 及 K_event(t) 统计独立；该噪声是扣除周期与事件后的残差项，驱动缓存命中率的高频抖动。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

traffic noise gaussian distribution standard deviation cache hit rate fluctuation
