# N71: 下游投影2：卖家净收益 R_seller 的均值与方差变化。R_seller = P_final * (1 - r) - C_hold(T)。干预后，P_fin

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N15

## Claim

下游投影2：卖家净收益 R_seller 的均值与方差变化。R_seller = P_final * (1 - r) - C_hold(T)。干预后，P_final 下降导致均值收入降低，但 T 延长导致持有成本 C_hold 增加。方差 Var(R_seller) 的变化取决于 Var(P) 和 Var(T) 的相对变化。若 Var(T) 增加幅度 > Var(P) 减小幅度，则卖家风险偏好者将受损更重。

## Corrected Claim

下游投影2：卖家净收益 R_seller 的均值与方差变化。R_seller = P_final * (1 - r) - C_hold(T)。干预后，P_final 下降导致均值收入降低，但 T 延长导致持有成本 C_hold 增加。方差 Var(R_seller) 的变化取决于 Var(P) 和 Var(T) 的相对变化。若 Var(T) 增加幅度 > Var(P) 减小幅度，则卖家风险偏好者将受损更重。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，均值变化方向符合代数逻辑（P降导致收入降，T增导致成本增），方差变化取决于各分量方差及协方差的相对大小，结论推导符合概率论基本性质。
