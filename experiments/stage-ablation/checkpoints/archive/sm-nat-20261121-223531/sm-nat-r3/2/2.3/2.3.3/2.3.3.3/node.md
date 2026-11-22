# N134: 蒙特卡洛模拟中 ΔH_corr 的非零估计条件：当 C' < S_total 时，LRU 保留对象集合由堆栈深度决定，LFU 由频率决定，ΔH_corr = H

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

蒙特卡洛模拟中 ΔH_corr 的非零估计条件：当 C' < S_total 时，LRU 保留对象集合由堆栈深度决定，LFU 由频率决定，ΔH_corr = H_LFU(C') - H_LRU(C')，需模拟 10,000 个对象的热度-大小联合分布（ρ=-0.3），计算两种策略下命中字节占比差值，预期 ΔH_corr 在 C'=0.5GB 时为 [待核验] 2-5 个百分点。

## Corrected Claim

蒙特卡洛模拟中 ΔH_corr 的非零估计条件：当 C' < S_total 时，LRU 保留对象集合由堆栈深度决定，LFU 由频率决定，ΔH_corr = H_LFU(C') - H_LRU(C')，需模拟 10,000 个对象的热度-大小联合分布（ρ=-0.3），计算两种策略下命中字节占比差值，预期 ΔH_corr 在 C'=0.5GB 时为非零值（具体数值需通过模拟验证）。

## Evidence

[质询]该陈述包含具体的经验性数值预测（ΔH_corr 在 C'=0.5GB 时为 2-5 个百分点），这属于特定参数下的模拟结果，无法从第一性原理直接推导，且参考来源未提供该具体数值的支持。 | 逻辑上，LRU 和 LFU 在热度-大小联合分布（ρ=-0.3）下确实会产生不同的命中字节占比，ΔH_corr 的定义和模拟方法在逻辑上是自洽的；但参考来源 [1] 仅介绍蒙特卡洛模拟的一般概念，与该具体事实（特定参数下的数值结果）无关，属于经验事实且缺乏直接来源支持。

## Search Query

LRU vs LFU hit rate Pareto distribution negative correlation simulation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/29323518696&rut=b7d5f1740358b7b2cad3caa56bc1d5cc2e37fb4daf10ea43f3f81712d8fb4361', 'type': 'ddg', 'title': '蒙特卡洛模拟快速上手（案例+Python代码） - 知乎'}
