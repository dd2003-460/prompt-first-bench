# N11: 卖家逐利约束：卖家目标最大化 E[Revenue] = P_deal × Prob(Sell|P_ask)，在信息不对称下，卖家无法精确估计 Prob(Sell

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N2

## Claim

卖家逐利约束：卖家目标最大化 E[Revenue] = P_deal × Prob(Sell|P_ask)，在信息不对称下，卖家无法精确估计 Prob(Sell)，导致定价偏离市场出清价格。

## Corrected Claim

卖家逐利约束：卖家目标最大化 E[Revenue] = P_deal × Prob(Sell|P_ask)，在信息不对称下，卖家无法精确估计 Prob(Sell)，导致定价偏离市场出清价格。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应信息不对称的微观基础（估计误差）、最优化过程（一阶条件）以及最终结果（偏差量化），逻辑层层递进且互不重叠，完整覆盖了父节点中关于目标函数、信息不对称机制及定价偏离结论的所有关键方面。）
