# N34: 有限样本修正：在 N=100,000 的离散对象集合中，最大对象大小 s_(N) 服从极值分布，其尺度约为 s_min * (N)^{1/α} = 10KB *

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

有限样本修正：在 N=100,000 的离散对象集合中，最大对象大小 s_(N) 服从极值分布，其尺度约为 s_min * (N)^{1/α} = 10KB * 100000^{1/1.1} ≈ 10KB * 10^4.545 ≈ 350MB，实际稳态方差由该极值主导而非无穷大。

## Corrected Claim

有限样本修正：在 N=100,000 的离散对象集合中，最大对象大小 s_(N) 服从极值分布，其尺度约为 s_min * (N)^{1/α} = 10KB * 100000^{1/1.1} ≈ 10KB * 10^4.545 ≈ 350MB，实际稳态方差由该极值主导而非无穷大。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布（α=1.1）的极值理论，最大值的期望量级确实由 N^(1/α) 决定，计算 100000^(1/1.1) ≈ 10^4.545 ≈ 35000，乘以 10KB 得到 350MB，数值量级与推导逻辑自洽。

## Search Query

order statistics Pareto maximum value estimation
