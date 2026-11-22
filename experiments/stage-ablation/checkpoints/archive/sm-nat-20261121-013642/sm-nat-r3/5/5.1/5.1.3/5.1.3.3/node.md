# N205: 在 Pareto(α=1.1) 大小分布下，缓存中对象的驻留时间 T_residence 与对象大小 s 呈负相关：T_residence(s) ≈ C / (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

在 Pareto(α=1.1) 大小分布下，缓存中对象的驻留时间 T_residence 与对象大小 s 呈负相关：T_residence(s) ≈ C / (R_bytes * P(s in cache | s))，大对象因占用空间多而驱逐快，导致按字节加权的平均折损因子 f_update_weighted = Σ (r_i * s_i * f_update(T_i)) / Σ (r_i * s_i) 显著低于按对象计数的平均 f_update，需通过数值积分计算加权值。

## Corrected Claim

在 Pareto(α=1.1) 大小分布下，缓存中对象的驻留时间 T_residence 与对象大小 s 呈负相关：T_residence(s) ≈ C / (R_bytes * P(s in cache | s))，大对象因占用空间多而驱逐快，导致按字节加权的平均折损因子 f_update_weighted = Σ (r_i * s_i * f_update(T_i)) / Σ (r_i * s_i) 显著低于按对象计数的平均 f_update，需通过数值积分计算加权值。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布下大对象占比高且易被驱逐，导致按字节加权的平均折损因子低于按对象计数的平均值，符合缓存替换策略（如LRU/FIFO）的基本直觉与数学性质。
