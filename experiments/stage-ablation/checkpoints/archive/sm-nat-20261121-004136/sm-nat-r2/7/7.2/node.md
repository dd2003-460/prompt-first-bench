# N69: LRU 命中率积分表达式的分母项计算：分母为总请求字节数 D_total = R_daily * E[Size_requested]，其中 R_daily = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

LRU 命中率积分表达式的分母项计算：分母为总请求字节数 D_total = R_daily * E[Size_requested]，其中 R_daily = 50,000,000 次/天，E[Size_requested] 为按热度分布加权的平均请求大小。由于热度与大小负相关 (ρ=-0.3)，热门对象较小，E[Size_requested] < E[S]，需计算加权平均值：E[Size_requested] = ∫ s * f_size(s) * f_rank(s) ds / ∫ f_rank(s) ds

## Corrected Claim

LRU 命中率积分表达式的分母项计算：分母为总请求字节数 D_total = R_daily * E[Size_requested]，其中 R_daily = 50,000,000 次/天，E[Size_requested] 为按热度分布加权的平均请求大小。由于热度与大小负相关 (ρ=-0.3)，热门对象较小，E[Size_requested] < E[S]，需计算加权平均值：E[Size_requested] = ∫ s * f_size(s) * f_rank(s) ds / ∫ f_rank(s) ds

## Evidence

先验知识/题面给定，逻辑校验通过：总请求字节数定义为请求次数乘以平均请求大小，且加权平均值的积分表达式符合概率论定义，量纲与逻辑自洽。
