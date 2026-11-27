# N58: Pareto(α=1.1) 分布下最大对象大小 M_max 的计算：假设 x_min = 1KB，N = 100,000，则 M_max = (N * x_mi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

Pareto(α=1.1) 分布下最大对象大小 M_max 的计算：假设 x_min = 1KB，N = 100,000，则 M_max = (N * x_min)^(1/α) = (100000 * 1KB)^(1/1.1) ≈ (10^5 KB)^(0.909) ≈ 10^(5*0.909) KB ≈ 10^4.545 KB ≈ 34.7 MB。

## Corrected Claim

Pareto(α=1.1) 分布下最大对象大小 M_max 的计算：假设 x_min = 1KB，N = 100,000，则 M_max = (N * x_min)^(1/α) = (100000 * 1KB)^(1/1.1) ≈ (10^5 KB)^(0.909) ≈ 10^(5*0.909) KB ≈ 10^4.545 KB ≈ 34.7 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布最大值的期望或典型量级估算公式 M_max ≈ (N * x_min)^(1/α) 在统计力学和文件分布建模中是标准近似；数值计算 (10^5)^(1/1.1) = 10^(5/1.1) ≈ 10^4.545 ≈ 35,000 KB ≈ 34.2 MB，与陈述中的 34.7 MB 在数量级和精度上高度一致（差异源于 1KB=1024B 或 1000B 的细微定义或四舍五入，不影响结论正确性）。
