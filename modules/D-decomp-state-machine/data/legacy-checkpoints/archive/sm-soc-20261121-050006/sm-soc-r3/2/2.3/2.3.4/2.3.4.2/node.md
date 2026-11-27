# N206: GMV损失项（ΔGMV_loss）的量化：ΔGMV_loss = P_median * Q_volume * (1 - (P_new / P_old)^η_pr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

GMV损失项（ΔGMV_loss）的量化：ΔGMV_loss = P_median * Q_volume * (1 - (P_new / P_old)^η_price)，其中 P_median 为基准价，Q_volume 为受影响成交量，η_price 为价格弹性系数（C2C市场通常 η_price ∈ [1.5, 2.5]），该公式将挂价下调转化为具体的营收损失数值。

## Corrected Claim

GMV损失项（ΔGMV_loss）的量化：ΔGMV_loss = P_median * Q_volume * (1 - (P_new / P_old)^η_price)，其中 P_median 为基准价，Q_volume 为受影响成交量，η_price 为价格弹性系数（C2C市场通常 η_price ∈ [1.5, 2.5]），该公式将挂价下调转化为具体的营收损失数值。

## Evidence

先验知识/题面给定，逻辑校验通过
