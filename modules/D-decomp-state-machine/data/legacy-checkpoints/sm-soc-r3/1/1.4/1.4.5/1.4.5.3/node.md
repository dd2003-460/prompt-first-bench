# N150: Success_rate_recent 的计算窗口偏差：过去 30 天成交溢价率 > 10% 的比例中，前 7 天数据权重为 0.4，后 23 天权重为 0.6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

Success_rate_recent 的计算窗口偏差：过去 30 天成交溢价率 > 10% 的比例中，前 7 天数据权重为 0.4，后 23 天权重为 0.6，以避免短期噪声主导更新过程，加权公式为 S_recent = 0.4 * S_7d + 0.6 * S_23d。

## Corrected Claim

Success_rate_recent 的计算窗口偏差：过去 30 天成交溢价率 > 10% 的比例中，前 7 天数据权重为 0.4，后 23 天权重为 0.6，以避免短期噪声主导更新过程，加权公式为 S_recent = 0.4 * S_7d + 0.6 * S_23d。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

weighted moving average success rate calculation window bias seller performance
