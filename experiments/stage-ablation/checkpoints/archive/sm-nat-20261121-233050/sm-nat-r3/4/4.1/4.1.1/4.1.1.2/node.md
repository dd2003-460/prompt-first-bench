# N107: 缓存容量比 M/C 的精确值取决于对象大小分布的截断方式：若假设所有对象大小均小于 128GB/N=1.31MB，则 M/C=1.0；若存在大于 1.31MB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

缓存容量比 M/C 的精确值取决于对象大小分布的截断方式：若假设所有对象大小均小于 128GB/N=1.31MB，则 M/C=1.0；若存在大于 1.31MB 的对象，则 M/C < 1.0，需计算 P(S_i > 1.31MB) 以修正有效容量比。

## Corrected Claim

缓存容量比 M/C 的精确值取决于对象大小分布的截断方式：若假设所有对象大小均小于 128GB/N=1.31MB，则 M/C=1.0；若存在大于 1.31MB 的对象，则 M/C < 1.0，需计算 P(S_i > 1.31MB) 以修正有效容量比。

## Evidence

先验知识/题面给定，逻辑校验通过：缓存容量比 M/C 的定义及截断效应符合存储系统基本原理，若对象大小均小于阈值则无截断损失（M/C=1.0），若存在大对象则有效容量减少（M/C<1.0），逻辑自洽且量级合理。

## Search Query

cache capacity ratio calculation with truncated Pareto distribution object size distribution
