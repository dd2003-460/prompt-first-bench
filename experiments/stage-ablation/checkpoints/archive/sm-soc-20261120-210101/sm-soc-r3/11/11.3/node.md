# N387: 新容忍阈值 θ_stop_new 的边界条件：当偏离度 D < θ_stop_new 时，买家点击率 CTR(D) 保持基线水平；当 D > θ_stop_ne

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

新容忍阈值 θ_stop_new 的边界条件：当偏离度 D < θ_stop_new 时，买家点击率 CTR(D) 保持基线水平；当 D > θ_stop_new 时，CTR(D) 呈指数衰减 CTR(D) = CTR_base * exp(-k * (D - θ_stop_new))。需确定衰减系数 k 以预测极端高溢价商品的流量损失。

## Corrected Claim

新容忍阈值 θ_stop_new 的边界条件：当偏离度 D < θ_stop_new 时，买家点击率 CTR(D) 保持基线水平；当 D > θ_stop_new 时，CTR(D) 呈指数衰减 CTR(D) = CTR_base * exp(-k * (D - θ_stop_new))。需确定衰减系数 k 以预测极端高溢价商品的流量损失。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

click through rate decay function price deviation online marketplace
