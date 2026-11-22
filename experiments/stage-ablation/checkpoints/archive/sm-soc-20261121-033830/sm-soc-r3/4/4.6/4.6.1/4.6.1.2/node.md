# N267: 成交概率模型 P(Sale|P, v) 的具体函数形式：P(Sale|P, v) = 1 / (1 + exp(-β0 - β1*(P-P_ref) - β2*

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

成交概率模型 P(Sale|P, v) 的具体函数形式：P(Sale|P, v) = 1 / (1 + exp(-β0 - β1*(P-P_ref) - β2*v))，其中 P_ref 为参考价格，β 为待估计系数，v 为卖家响应速度，需通过逻辑回归拟合历史数据 [待核验]

## Corrected Claim

成交概率模型 P(Sale|P, v) 的具体函数形式：P(Sale|P, v) = 1 / (1 + exp(-β0 - β1*(P-P_ref) - β2*v))，其中 P_ref 为参考价格，β 为待估计系数，v 为卖家响应速度，需通过逻辑回归拟合历史数据 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过
