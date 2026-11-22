# N77: Pareto(β=0.9) 边缘 CDF F_f(f) 的逆函数（分位数函数）Q_f(q) = f_min * q^{-1/β} = f_min * q^{-1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

Pareto(β=0.9) 边缘 CDF F_f(f) 的逆函数（分位数函数）Q_f(q) = f_min * q^{-1/β} = f_min * q^{-1/0.9}，其中 f_min 由总请求率 5000万/天 和对象数 10万 归一化确定，用于将 Copula 变量 v 映射回热度空间 f。

## Corrected Claim

Pareto(β=0.9) 边缘 CDF F_f(f) 的逆函数（分位数函数）Q_f(q) = f_min * q^{-1/β} = f_min * q^{-1/0.9}，其中 f_min 由总请求率 5000万/天 和对象数 10万 归一化确定，用于将 Copula 变量 v 映射回热度空间 f。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布逆CDF公式正确，归一化条件符合定义
