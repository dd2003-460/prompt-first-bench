# N162: 二阶条件（SOC）稳定性检验：$\frac{\partial^2 E[U_s]}{\partial P_{ask}^2} < 0$ 必须成立。若 $\frac{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

二阶条件（SOC）稳定性检验：$\frac{\partial^2 E[U_s]}{\partial P_{ask}^2} < 0$ 必须成立。若 $\frac{\partial^2 E[T_{sale}]}{\partial P_{ask}^2}$ 为正且绝对值过大，可能导致一阶条件解为局部极小值（即高挂价反而降低收益）。需验证在 $P_{ask} \in [1.1, 1.3]P_{ref}$ 区间内，SOC 是否恒为负。若 SOC 变号，则存在多重均衡或边界解。

## Corrected Claim

二阶条件（SOC）稳定性检验：$\frac{\partial^2 E[U_s]}{\partial P_{ask}^2} < 0$ 必须成立。若 $\frac{\partial^2 E[T_{sale}]}{\partial P_{ask}^2}$ 为正且绝对值过大，可能导致一阶条件解为局部极小值（即高挂价反而降低收益）。需验证在 $P_{ask} \in [1.1, 1.3]P_{ref}$ 区间内，SOC 是否恒为负。若 SOC 变号，则存在多重均衡或边界解。

## Evidence

先验知识/题面给定，逻辑校验通过：二阶条件（SOC）用于判断极值性质（负值对应极大值），若SOC变号确实意味着局部极小值或边界解，符合微积分基本定理及经济学最优化原理。
