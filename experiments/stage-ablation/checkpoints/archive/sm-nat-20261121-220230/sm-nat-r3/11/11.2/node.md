# N296: LRU 驻留集合（最小 K 个对象）的总大小 S_resident 的解析表达式：S_resident = ∫_{s_min}^{s_K} s * f_Pare

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

LRU 驻留集合（最小 K 个对象）的总大小 S_resident 的解析表达式：S_resident = ∫_{s_min}^{s_K} s * f_Pareto(s) ds，其中 s_K 为第 K 个最小对象的大小阈值，需通过逆 CDF 函数 s_K = s_min * (K/N)^(-1/(α-1)) 确定积分上限，代入 α=1.1, K=11900, N=100000 计算具体字节数。

## Corrected Claim

LRU 驻留集合（最小 K 个对象）的总大小 S_resident 的解析表达式：S_resident = ∫_{s_min}^{s_K} s * f_Pareto(s) ds，其中 s_K 为第 K 个最小对象的大小阈值，需通过逆 CDF 函数 s_K = s_min * (K/N)^(-1/(α-1)) 确定积分上限，代入 α=1.1, K=11900, N=100000 计算具体字节数。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU驻留集合定义为最小K个对象，其总大小确为对象大小在最小K个范围内的积分；Pareto分布逆CDF公式 s_K = s_min * (K/N)^(-1/(α-1)) 符合标准Pareto分布性质，量纲与逻辑自洽。
