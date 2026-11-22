# N39: 平台驱动强度 D_P 的计算公式：D_P = ∂S_eq/∂W_exposure * (∂W_exposure/∂Strategy_P)，其中 ∂W_expos

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

平台驱动强度 D_P 的计算公式：D_P = ∂S_eq/∂W_exposure * (∂W_exposure/∂Strategy_P)，其中 ∂W_exposure/∂Strategy_P 为平台策略变化对曝光权重的影响系数（假设流量倾斜策略下该系数为 0.5，默认展示下为 0），该公式揭示了平台通过调整曝光权重对均衡稳定性的边际贡献，用于与 D_S 和 D_B 进行对比。

## Corrected Claim

平台驱动强度 D_P 的计算公式：D_P = ∂S_eq/∂W_exposure * (∂W_exposure/∂Strategy_P)，其中 ∂W_exposure/∂Strategy_P 为平台策略变化对曝光权重的影响系数（假设流量倾斜策略下该系数为 0.5，默认展示下为 0），该公式揭示了平台通过调整曝光权重对均衡稳定性的边际贡献，用于与 D_S 和 D_B 进行对比。

## Evidence

先验知识/题面给定，逻辑校验通过
