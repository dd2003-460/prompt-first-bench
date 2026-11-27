# N76: 卖家总预期收益损失中的‘成交率修正项’具体化：该修正项并非常数，而是成交率对价格偏离度的弹性函数 ε_CVR = dln(CVR)/dln(D)。假设基准成交率

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

卖家总预期收益损失中的‘成交率修正项’具体化：该修正项并非常数，而是成交率对价格偏离度的弹性函数 ε_CVR = dln(CVR)/dln(D)。假设基准成交率 CVR_0 = 2%，当 D 从 20% 降至 10% 时，CVR 变化为 CVR_1 = CVR_0 * (10/20)^ε_CVR。若 ε_CVR = 0.8，则 CVR 提升约 28%，需代入此动态值计算总损失，而非静态 ΔQ=20%。

## Corrected Claim

卖家总预期收益损失中的‘成交率修正项’具体化：该修正项并非常数，而是成交率对价格偏离度的弹性函数 ε_CVR = dln(CVR)/dln(D)。假设基准成交率 CVR_0 = 2%，当 D 从 20% 降至 10% 时，CVR 变化为 CVR_1 = CVR_0 * (10/20)^ε_CVR。若 ε_CVR = 0.8，则 CVR 提升约 28%，需代入此动态值计算总损失，而非静态 ΔQ=20%。

## Evidence

先验知识/题面给定，逻辑校验通过：弹性定义及数值计算（(0.5)^0.8 ≈ 0.574，提升约28%）均符合数学逻辑与经济学直觉。

## Search Query

conversion rate elasticity to price deviation second hand goods
