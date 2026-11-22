# N212: 未售出概率 P_loss 的时间动态模型：P_loss(t) = 1 - exp(-t / T_median_sale)，其中 T_median_sale 为同

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

未售出概率 P_loss 的时间动态模型：P_loss(t) = 1 - exp(-t / T_median_sale)，其中 T_median_sale 为同类商品历史成交周期的中位数，需从平台历史数据中提取 T_median_sale 的具体数值（如7天）。

## Corrected Claim

未售出概率 P_loss 的时间动态模型：P_loss(t) = 1 - exp(-t / T_median_sale)，其中 T_median_sale 为同类商品历史成交周期的中位数，需从平台历史数据中提取 T_median_sale 的具体数值（如7天）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

second hand market median selling time distribution exponential decay
