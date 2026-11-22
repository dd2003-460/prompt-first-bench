# N60: 基于 Pareto(β=0.9) 热度分布，计算第 i 个对象的请求频率 f_i = C * i^{-β}，其中 C 为归一化常数，使得 Sum(f_i) = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

基于 Pareto(β=0.9) 热度分布，计算第 i 个对象的请求频率 f_i = C * i^{-β}，其中 C 为归一化常数，使得 Sum(f_i) = 1

## Corrected Claim

基于 Pareto(β=0.9) 热度分布，计算第 i 个对象的请求频率 f_i = C * i^{-β}，其中 C 为归一化常数，使得 Sum(f_i) = 1

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别处理了归一化常数的计算、离散与连续近似的误差分析、以及有限总体截断带来的边界效应。三者关注点不同（计算值、精度误差、边界条件），互不重叠且无矛盾，共同构成了从理论公式到工程实现的关键考量。）
