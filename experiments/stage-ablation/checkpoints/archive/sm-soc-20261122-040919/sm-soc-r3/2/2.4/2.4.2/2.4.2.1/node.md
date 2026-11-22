# N229: 共享随机源定义：买家效用加成权重 w_signal 并非固定常数，而是随平台实时数据反馈调整的随机变量，其分布为 w_signal ~ N(w_0, σ²_w)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N62

## Claim

共享随机源定义：买家效用加成权重 w_signal 并非固定常数，而是随平台实时数据反馈调整的随机变量，其分布为 w_signal ~ N(w_0, σ²_w)，其中 w_0 为基准权重，σ²_w 由平台算法更新频率 f_update 和样本量 n_sample 决定，σ²_w ∝ 1/(f_update * n_sample)。

## Corrected Claim

共享随机源定义：买家效用加成权重 w_signal 并非固定常数，而是随平台实时数据反馈调整的随机变量，其分布为 w_signal ~ N(w_0, σ²_w)，其中 w_0 为基准权重，σ²_w 由平台算法更新频率 f_update 和样本量 n_sample 决定，σ²_w ∝ 1/(f_update * n_sample)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dynamic weight adjustment in buyer utility function recommendation system
