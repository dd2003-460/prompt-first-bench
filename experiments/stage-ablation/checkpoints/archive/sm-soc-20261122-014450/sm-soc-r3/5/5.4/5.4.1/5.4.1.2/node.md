# N302: 平台算法反馈项系数 β_platform 的量化表达式：β_platform = W_gmv * (∂R_exposure/∂P_list) * (1/τ_ad

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

平台算法反馈项系数 β_platform 的量化表达式：β_platform = W_gmv * (∂R_exposure/∂P_list) * (1/τ_adjust)，其中 W_gmv ∈ [0.6, 0.9] 为GMV权重，∂R_exposure/∂P_list ∈ [0.05, 0.15] 为曝光率对价格的偏导，τ_adjust ∈ [1, 3] 天为算法更新周期。

## Corrected Claim

平台算法反馈项系数 β_platform 的量化表达式：β_platform = W_gmv * (∂R_exposure/∂P_list) * (1/τ_adjust)，其中 W_gmv ∈ [0.6, 0.9] 为GMV权重，∂R_exposure/∂P_list ∈ [0.05, 0.15] 为曝光率对价格的偏导，τ_adjust ∈ [1, 3] 天为算法更新周期。

## Evidence

先验知识/题面给定，逻辑校验通过
