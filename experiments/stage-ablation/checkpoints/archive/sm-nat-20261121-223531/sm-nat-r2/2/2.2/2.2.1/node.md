# N40: 工作点 1 中 h_median 的具体数值计算：基于 Pareto(β=0.9) 和 100k 对象总数，热度中位数 h_median 对应累积概率 0.5 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

工作点 1 中 h_median 的具体数值计算：基于 Pareto(β=0.9) 和 100k 对象总数，热度中位数 h_median 对应累积概率 0.5 的分位数，即 h_median = h_min * (1/0.5)^{1/(1-β)} = h_min * 2^{10}。若归一化 h_min=1，则 h_median=1024，代表第 50,000 名对象的请求频率。

## Corrected Claim

工作点 1 中 h_median 的具体数值计算：基于 Pareto(β=0.9) 和 100k 对象总数，热度中位数 h_median 对应累积概率 0.5 的分位数，即 h_median = h_min * (1/0.5)^{1/(1-β)} = h_min * 2^{10}。若归一化 h_min=1，则 h_median=1024，代表第 50,000 名对象的请求频率。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布分位数公式推导正确，2^10=1024计算无误，中位数对应累积概率0.5及第50,000名对象的定义符合统计学原理。
