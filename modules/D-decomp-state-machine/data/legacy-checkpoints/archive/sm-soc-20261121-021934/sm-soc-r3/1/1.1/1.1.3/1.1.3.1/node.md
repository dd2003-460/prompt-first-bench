# N65: 买家价格异常阈值 θ_buyer 的量化：θ_buyer = k_θ * σ_ε，其中 k_θ 为买家风险偏好系数（保守型 k_θ=2.0，激进型 k_θ=1.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

买家价格异常阈值 θ_buyer 的量化：θ_buyer = k_θ * σ_ε，其中 k_θ 为买家风险偏好系数（保守型 k_θ=2.0，激进型 k_θ=1.0），该值可通过买家对价格偏离度的点击率断点回归估计，断点位置即为 θ_buyer。

## Corrected Claim

买家价格异常阈值 θ_buyer 的量化：θ_buyer = k_θ * σ_ε，其中 k_θ 为买家风险偏好系数（保守型 k_θ=2.0，激进型 k_θ=1.0），该值可通过买家对价格偏离度的点击率断点回归估计，断点位置即为 θ_buyer。

## Evidence

先验知识/题面给定，逻辑校验通过
