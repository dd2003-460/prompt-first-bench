# N48: 期望收入最大化的一阶条件：dE[Revenue]/dP_ask = Prob(Sell|P_ask) + P_deal × dProb(Sell|P_ask)/

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N11

## Claim

期望收入最大化的一阶条件：dE[Revenue]/dP_ask = Prob(Sell|P_ask) + P_deal × dProb(Sell|P_ask)/dP_ask = 0；在信息不对称下，卖家使用的 dProb/dP_ask 斜率绝对值小于真实市场弹性，导致最优 P_ask* 高于市场出清价 P_clear。

## Corrected Claim

期望收入最大化的一阶条件：dE[Revenue]/dP_ask = Prob(Sell|P_ask) + P_deal × dProb(Sell|P_ask)/dP_ask = 0；在信息不对称下，卖家使用的 dProb/dP_ask 斜率绝对值小于真实市场弹性，导致最优 P_ask* 高于市场出清价 P_clear。

## Evidence

先验知识/题面给定，逻辑校验通过：期望收入函数求导符合乘积法则，信息不对称导致卖家低估价格敏感度（斜率绝对值偏小），从而推导出的最优定价高于市场出清价，符合经济学直觉。
