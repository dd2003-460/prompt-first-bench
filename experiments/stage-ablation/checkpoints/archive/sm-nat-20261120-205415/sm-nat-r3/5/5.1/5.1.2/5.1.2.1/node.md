# N182: N67中 K=100 的假设基于平均对象大小 1.28MB (128GB/100)，但 Pareto(α=1.1) 分布下缓存前 K 个对象的大小累积 ∑_{i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

N67中 K=100 的假设基于平均对象大小 1.28MB (128GB/100)，但 Pareto(α=1.1) 分布下缓存前 K 个对象的大小累积 ∑_{i=1}^K s_i 随 K 增长极慢（因头部对象极大），实际 K 远小于 100，需通过 ∫_{x_min}^{S_K} x f(x) dx = 128GB 数值求解 S_K 和 K

## Corrected Claim

N67中 K=100 的假设基于平均对象大小 1.28MB (128GB/100)，但 Pareto(α=1.1) 分布下缓存前 K 个对象的大小累积 ∑_{i=1}^K s_i 随 K 增长极慢（因头部对象极大），实际 K 远小于 100，需通过 ∫_{x_min}^{S_K} x f(x) dx = 128GB 数值求解 S_K 和 K

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)具有重尾特性，头部对象占据绝大部分空间，导致累积大小达到128GB所需的对象数量K远小于基于平均大小计算的100，需通过积分求解，逻辑自洽且符合统计规律。
