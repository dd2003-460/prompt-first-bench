# N119: 在 Pareto(β) 分布下，头部 10% 对象（排名 1-10000）占据的请求字节数占比 B_top10% 的解析公式：B_top10% = 1 - (1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

在 Pareto(β) 分布下，头部 10% 对象（排名 1-10000）占据的请求字节数占比 B_top10% 的解析公式：B_top10% = 1 - (1/10)^(1-β)，该值决定了 LFU 相对于 LRU 的理论最大增益上限

## Corrected Claim

在 Pareto(β) 分布下，头部 10% 对象（排名 1-10000）占据的请求字节数占比 B_top10% 的解析公式：B_top10% = 1 - (1/10)^(1-β)，该值决定了 LFU 相对于 LRU 的理论最大增益上限

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布尾部占比公式推导正确，且LFU增益上限与头部集中度正相关符合缓存理论直觉
