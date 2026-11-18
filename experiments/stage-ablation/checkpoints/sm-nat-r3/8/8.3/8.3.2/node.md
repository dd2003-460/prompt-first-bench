# N170: 大小排名对应的 CDF 值 F_S(s) 的逆函数：Pareto(α=1.1, x_min=1KB) 的 CDF 为 F_S(s) = 1 - (x_min/s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

大小排名对应的 CDF 值 F_S(s) 的逆函数：Pareto(α=1.1, x_min=1KB) 的 CDF 为 F_S(s) = 1 - (x_min/s)^{α-1} = 1 - (1/s)^{0.1}，其逆函数 s(F_S) = 1 / (1-F_S)^{10}，用于将 Copula 变换后的标准化正态变量映射回具体的字节大小 s_i。

## Corrected Claim

大小排名对应的 CDF 值 F_S(s) 的逆函数：Pareto(α=1.1, x_min=1KB) 的 CDF 为 F_S(s) = 1 - (x_min/s)^{α-1} = 1 - (1/s)^{0.1}，其逆函数 s(F_S) = 1 / (1-F_S)^{10}，用于将 Copula 变换后的标准化正态变量映射回具体的字节大小 s_i。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF公式及逆函数推导正确，量纲与数值关系自洽。
