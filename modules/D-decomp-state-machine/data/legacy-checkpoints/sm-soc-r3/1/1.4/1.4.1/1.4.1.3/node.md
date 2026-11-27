# N138: P_hist_avg 的长期基准定义：P_hist_avg 为过去 180 天的成交均价，用于捕捉季节性波动，若 180 天数据不足则回退至 365 天，数据缺

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

P_hist_avg 的长期基准定义：P_hist_avg 为过去 180 天的成交均价，用于捕捉季节性波动，若 180 天数据不足则回退至 365 天，数据缺失时权重 w_3 归零并重新归一化 w_1, w_2

## Corrected Claim

P_hist_avg 的长期基准定义：P_hist_avg 为过去 180 天的成交均价，用于捕捉季节性波动，若 180 天数据不足则回退至 365 天，数据缺失时权重 w_3 归零并重新归一化 w_1, w_2

## Evidence

先验知识/题面给定，逻辑校验通过
