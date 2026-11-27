# N5: 缓存容量约束下的对象覆盖数 K = min(100000, floor(128GB / 100KB))，假设对象平均大小 100KB（基于 Pareto(α=1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存容量约束下的对象覆盖数 K = min(100000, floor(128GB / 100KB))，假设对象平均大小 100KB（基于 Pareto(α=1.1) 截断分布的近似均值），K ≈ 1310720 > 100000，故容量非瓶颈，可缓存全部对象

## Corrected Claim

缓存容量约束下的对象覆盖数 K = min(100000, floor(128GB / 100KB))，假设对象平均大小 100KB（基于 Pareto(α=1.1) 截断分布的近似均值），K ≈ 1310720 > 100000，故容量非瓶颈，可缓存全部对象

## Evidence

先验知识/题面给定，逻辑校验通过：128GB / 100KB = 1310720，且 1310720 > 100000，min 运算结果正确，结论自洽。
