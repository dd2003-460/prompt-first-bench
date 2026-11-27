# N17: 卖家响应函数：在价格信号 p_t 下，卖家降价概率 P(decrease|p_t) = f(边际效用损失, 机会成本, 心理账户效应)，具体需量化当前高挂价策略

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

卖家响应函数：在价格信号 p_t 下，卖家降价概率 P(decrease|p_t) = f(边际效用损失, 机会成本, 心理账户效应)，具体需量化当前高挂价策略的预期收益 E[R_high] vs 降价后预期收益 E[R_low]，其中 E[R] = Price * P(sale|Price) - C_holding。

## Corrected Claim

卖家响应函数：在价格信号 p_t 下，卖家降价概率 P(decrease|p_t) = f(边际效用损失, 机会成本, 心理账户效应)，具体需量化当前高挂价策略的预期收益 E[R_high] vs 降价后预期收益 E[R_low]，其中 E[R] = Price * P(sale|Price) - C_holding。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了基于期望效用理论（Expected Utility Theory）和前景理论（Prospect Theory，涉及心理账户/损失厌恶）的卖家决策模型。公式 E[R] = Price * P(sale|Price) - C_holding 符合基本的经济学收益定义（期望收入减去持有成本），逻辑自洽且量纲合理。
