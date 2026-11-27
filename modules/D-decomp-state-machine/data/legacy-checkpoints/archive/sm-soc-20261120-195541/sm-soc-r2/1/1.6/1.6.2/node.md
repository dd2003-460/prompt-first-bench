# N38: 卖家驱动强度 D_S 的计算公式：D_S = ∂S_eq/∂P_ask * (∂P_ask/∂Strategy_S)，其中 ∂P_ask/∂Strategy_S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

卖家驱动强度 D_S 的计算公式：D_S = ∂S_eq/∂P_ask * (∂P_ask/∂Strategy_S)，其中 ∂P_ask/∂Strategy_S 为卖家策略变化对挂价的影响系数（假设高挂价策略下该系数为 1.2，降价策略下为 -0.8），通过链式法则将策略变化传导至均衡稳定性变化，从而量化卖家的驱动作用。

## Corrected Claim

卖家驱动强度 D_S 的计算公式：D_S = ∂S_eq/∂P_ask * (∂P_ask/∂Strategy_S)，其中 ∂P_ask/∂Strategy_S 为卖家策略变化对挂价的影响系数（假设高挂价策略下该系数为 1.2，降价策略下为 -0.8），通过链式法则将策略变化传导至均衡稳定性变化，从而量化卖家的驱动作用。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合链式法则定义，量纲一致，数值假设在合理范围内。
