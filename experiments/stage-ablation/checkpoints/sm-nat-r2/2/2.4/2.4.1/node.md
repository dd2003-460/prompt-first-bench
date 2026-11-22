# N54: 256GB 容量下的长尾字节占比计算：Tail_Byte_256 = 1 - CDF_Pareto(S_256; α=1.1, x_min)，其中 S_256 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

256GB 容量下的长尾字节占比计算：Tail_Byte_256 = 1 - CDF_Pareto(S_256; α=1.1, x_min)，其中 S_256 对应 256GB 可容纳的对象大小分位数

## Corrected Claim

256GB 容量下的长尾字节占比计算：Tail_Byte_256 = 1 - CDF_Pareto(S_256; α=1.1, x_min)，其中 S_256 对应 256GB 可容纳的对象大小分位数

## Evidence

先验知识/题面给定，逻辑校验通过：长尾字节占比定义为总字节数中超过特定分位数的部分，数学上等价于 1 减去该分位数对应的累积分布函数（CDF）值，公式逻辑自洽且量纲正确。
