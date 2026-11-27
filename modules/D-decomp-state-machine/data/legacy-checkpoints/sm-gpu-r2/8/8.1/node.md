# N93: 保守估计值计算公式：当价格数据被标记为[待核验]或[Stale_Risk]时，TCO计算中使用的价格 P_conservative = P_memory * (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26, N27, N28

## Claim

保守估计值计算公式：当价格数据被标记为[待核验]或[Stale_Risk]时，TCO计算中使用的价格 P_conservative = P_memory * (1 + CV_price)，其中 CV_price 为该硬件类别近6个月价格波动系数（通常取0.10-0.15）。

## Corrected Claim

保守估计值计算公式：当价格数据被标记为[待核验]或[Stale_Risk]时，TCO计算中使用的价格 P_conservative = P_memory * (1 + CV_price)，其中 CV_price 为该硬件类别近6个月价格波动系数（通常取0.10-0.15）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合保守估计的常规逻辑（基准价乘以波动系数），CV_price取值范围0.10-0.15在硬件市场波动中属于合理量级，无内部矛盾。
