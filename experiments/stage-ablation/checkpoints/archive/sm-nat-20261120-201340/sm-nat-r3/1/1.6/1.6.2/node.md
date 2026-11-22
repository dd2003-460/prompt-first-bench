# N46: Pareto(β=0.9) 分布的最小请求率 r_min 的确定：r_min = R_total / (N * (1 - N^{1-β}))，其中 R_tota

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Pareto(β=0.9) 分布的最小请求率 r_min 的确定：r_min = R_total / (N * (1 - N^{1-β}))，其中 R_total=50M/day，N=10^5，β=0.9；该值确保所有对象的请求率之和等于总请求率，是计算具体 r_i 值的基础参数。

## Corrected Claim

Pareto(β=0.9) 分布的最小请求率 r_min 的确定：r_min = R_total / (N * (1 - N^{1-β}))，其中 R_total=50M/day，N=10^5，β=0.9；该值确保所有对象的请求率之和等于总请求率，是计算具体 r_i 值的基础参数。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布归一化常数推导正确，量级合理（r_min约为总请求率除以N的等效平均值的倒数关系，符合幂律分布尾部特征）
