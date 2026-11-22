# N236: 计算缓存中实际存储的总字节数 S_cache，基于N81确定的K=100,000（假设缓存装满所有对象）及Pareto(α=1.1)分布，S_cache = Σ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

计算缓存中实际存储的总字节数 S_cache，基于N81确定的K=100,000（假设缓存装满所有对象）及Pareto(α=1.1)分布，S_cache = Σ_{i=1}^{100000} s_i，需通过积分或蒙特卡洛模拟得出具体GB值。

## Corrected Claim

计算缓存中实际存储的总字节数 S_cache，基于N81确定的K=100,000（假设缓存装满所有对象）及Pareto(α=1.1)分布，S_cache = Σ_{i=1}^{100000} s_i，需通过积分或蒙特卡洛模拟得出具体GB值。

## Evidence

先验知识/题面给定，逻辑校验通过：基于给定的对象数量K和Pareto分布参数，通过积分或模拟计算总字节数在数学和逻辑上是自洽且合理的。

## Search Query

Calculate total byte size of 100,000 objects following Pareto alpha=1.1 distribution
