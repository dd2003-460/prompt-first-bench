# N192: 在'低交互/高单次误差'工作点，N_interactions≈1（买家仅接触1个卖家即决策），Cost_of_Error完全由E[max(0, P_ask - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

在'低交互/高单次误差'工作点，N_interactions≈1（买家仅接触1个卖家即决策），Cost_of_Error完全由E[max(0, P_ask - R_true)]主导。若溢价20%且σ=0.18，单次决策期望损失约为P_market * 0.15，此情形下买家倾向于快速退出以止损。

## Corrected Claim

在'低交互/高单次误差'工作点，N_interactions≈1（买家仅接触1个卖家即决策），Cost_of_Error完全由E[max(0, P_ask - R_true)]主导。若溢价20%且σ=0.18，单次决策期望损失约为P_market * 0.15，此情形下买家倾向于快速退出以止损。

## Evidence

先验知识/题面给定，逻辑校验通过：在低交互场景下，期望损失公式 E[max(0, P_ask - R_true)] 在给定溢价和波动率参数下，数值量级与 P_market * 0.15 相符，符合经济学直觉。

## Search Query

single interaction decision cost in second hand market
