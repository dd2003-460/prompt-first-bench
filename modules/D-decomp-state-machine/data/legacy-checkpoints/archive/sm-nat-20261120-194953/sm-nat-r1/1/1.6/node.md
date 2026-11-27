# N11: 工作点 2（基于频率阈值的近似）：将 LRU 近似为保留访问频率高于阈值 $f_{th}$ 的对象，利用 Pareto 分布尾部的累积质量计算满足 $\sum_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

工作点 2（基于频率阈值的近似）：将 LRU 近似为保留访问频率高于阈值 $f_{th}$ 的对象，利用 Pareto 分布尾部的累积质量计算满足 $\sum_{i: R_i > f_{th}} S_i \le 128$ GB 的 $f_{th}$，并据此估算命中率。

## Corrected Claim

工作点 2（基于频率阈值的近似）：将 LRU 近似为保留访问频率高于阈值 $f_{th}$ 的对象，利用 Pareto 分布尾部的累积质量计算满足 $\sum_{i: R_i > f_{th}} S_i \le 128$ GB 的 $f_{th}$，并据此估算命中率。

## Evidence

先验知识/题面给定，逻辑校验通过
