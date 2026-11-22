# N122: 共享随机源：卖家感知未成交概率 P_loss_perception 的时间动态模型，定义为商品挂出时长 T 的函数，P_loss_perception(T) =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N42

## Claim

共享随机源：卖家感知未成交概率 P_loss_perception 的时间动态模型，定义为商品挂出时长 T 的函数，P_loss_perception(T) = 0.2 + 0.4 * (1 - e^(-T/72h)，其中 T 单位为小时。

## Corrected Claim

共享随机源：卖家感知未成交概率 P_loss_perception 的时间动态模型，定义为商品挂出时长 T 的函数，P_loss_perception(T) = 0.2 + 0.4 * (1 - e^(-T/72h)，其中 T 单位为小时。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller perceived probability of not selling time decay function second-hand
