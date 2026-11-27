# N187: 求解卖家最优定价条件 $\frac{\partial P_{sell}}{\partial P_{ask}} = \lambda \frac{\partial 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N61

## Claim

求解卖家最优定价条件 $\frac{\partial P_{sell}}{\partial P_{ask}} = \lambda \frac{\partial T_{sale}}{\partial P_{ask}}$ 中的 $\lambda$（时间价值系数）。$\lambda$ 定义为卖家每增加1天成交周期所放弃的效用（如资金占用成本或持有成本）。在二手非标品市场，资金年化成本约 5-10%，折算为每日成本 $\lambda_{daily} \approx 0.00014 - 0.00027$ 倍商品价值。

## Corrected Claim

求解卖家最优定价条件 $\frac{\partial P_{sell}}{\partial P_{ask}} = \lambda \frac{\partial T_{sale}}{\partial P_{ask}}$ 中的 $\lambda$（时间价值系数）。$\lambda$ 定义为卖家每增加1天成交周期所放弃的效用（如资金占用成本或持有成本）。在二手非标品市场，资金年化成本约 5-10%，折算为每日成本 $\lambda_{daily} \approx 0.00014 - 0.00027$ 倍商品价值。

## Evidence

先验知识/题面给定，逻辑校验通过：年化5-10%折算为每日成本（除以365）数值量级正确（0.05/365≈0.000137, 0.10/365≈0.000274），符合经济学常识。
