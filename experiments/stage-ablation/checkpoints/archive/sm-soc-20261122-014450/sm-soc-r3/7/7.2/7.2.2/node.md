# N366: 曝光率提升 10% 导致周期缩短 5-8% 的边界条件：该线性近似仅在曝光率变化 Δln(Exposure) ∈ [-0.1, 0.1] 区间内有效；若 Δln

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

曝光率提升 10% 导致周期缩短 5-8% 的边界条件：该线性近似仅在曝光率变化 Δln(Exposure) ∈ [-0.1, 0.1] 区间内有效；若 Δln(Exposure) > 0.1，需引入二次项 β*(Δln(Exposure))^2 以捕捉边际效应递减，β 需通过数据估计。

## Corrected Claim

曝光率提升 10% 导致周期缩短 5-8% 的边界条件：该线性近似仅在曝光率变化 Δln(Exposure) ∈ [-0.1, 0.1] 区间内有效；若 Δln(Exposure) > 0.1，需引入二次项 β*(Δln(Exposure))^2 以捕捉边际效应递减，β 需通过数据估计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

diminishing returns exposure increase transaction time nonlinear effect
