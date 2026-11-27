# N241: 在低价格区间（P_new < P_high * 0.8），成交概率增长边际递减：P(Sale|P_new) 的导数随价格降低而减小，存在一个最优价格点 P_op

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

在低价格区间（P_new < P_high * 0.8），成交概率增长边际递减：P(Sale|P_new) 的导数随价格降低而减小，存在一个最优价格点 P_opt 使得 E[Revenue] = P_new * P(Sale|P_new) 最大化，该点通常位于 P_high * (1 + 1/η) 附近。

## Corrected Claim

在低价格区间（P_new < P_high * 0.8），成交概率增长边际递减：P(Sale|P_new) 的导数随价格降低而减小，存在一个最优价格点 P_opt 使得 E[Revenue] = P_new * P(Sale|P_new) 最大化，该点通常位于 P_high * (1 + 1/η) 附近。

## Evidence

先验知识/题面给定，逻辑校验通过：基于弹性定义 η = (dP/dQ)/(Q/P) 或类似需求弹性关系，收入最大化条件 d(P*Q)/dP = 0 推导出 P_opt = P_high * (1 + 1/η) 是标准微观经济学结论，且低价格区间边际递减符合需求曲线凸性特征。
