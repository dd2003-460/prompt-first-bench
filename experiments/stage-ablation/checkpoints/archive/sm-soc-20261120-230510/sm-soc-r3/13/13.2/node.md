# N322: 定向压力项 (P-V) 的梯度计算：∇Fitness/∇P_ask = Prob(Sell|P_ask) - P_ask * ∂Prob(Sell)/∂P_as

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

定向压力项 (P-V) 的梯度计算：∇Fitness/∇P_ask = Prob(Sell|P_ask) - P_ask * ∂Prob(Sell)/∂P_ask，该梯度为正表示增加挂价能提升期望利润，为负表示应降价；均衡点满足 ∇Fitness = 0，即 1 = (P_ask/Prob(Sell)) * (∂Prob(Sell)/∂P_ask)。

## Corrected Claim

定向压力项 (P-V) 的梯度计算：∇Fitness/∇P_ask = Prob(Sell|P_ask) - P_ask * ∂Prob(Sell)/∂P_ask，该梯度为正表示增加挂价能提升期望利润，为负表示应降价；均衡点满足 ∇Fitness = 0，即 1 = (P_ask/Prob(Sell)) * (∂Prob(Sell)/∂P_ask)。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

gradient of expected profit with respect to ask price
