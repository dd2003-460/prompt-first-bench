# N35: 平台策略‘流量倾斜’的权重函数：W_exposure = W_base * (1 + β_platform * (P_ask/P_market - 1))^k，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

平台策略‘流量倾斜’的权重函数：W_exposure = W_base * (1 + β_platform * (P_ask/P_market - 1))^k，其中 k 为指数参数（假设 k=1.5），β_platform 为平台对高溢价商品的偏好系数（如 N21 所述 β_platform ≈ 0.3），该函数决定了在纳什均衡中，平台如何放大高挂价商品的曝光以维持均衡稳定性。

## Corrected Claim

平台策略‘流量倾斜’的权重函数：W_exposure = W_base * (1 + β_platform * (P_ask/P_market - 1))^k，其中 k 为指数参数（假设 k=1.5），β_platform 为平台对高溢价商品的偏好系数（如 N21 所述 β_platform ≈ 0.3），该函数决定了在纳什均衡中，平台如何放大高挂价商品的曝光以维持均衡稳定性。

## Evidence

先验知识/题面给定，逻辑校验通过
