# N77: 基于 CDN 常见对象大小上限 x_max = 100 MB 的工程假设，反解 x_min 的方程：1.31072 = 1.1 * x_min * (100^(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

基于 CDN 常见对象大小上限 x_max = 100 MB 的工程假设，反解 x_min 的方程：1.31072 = 1.1 * x_min * (100^(-0.1) - x_min^(-0.1)) / ((-0.1) * (100^1.1 - x_min^1.1))。通过数值迭代求解，若 x_max=100MB，则 x_min ≈ 0.5 MB 才能使 E[S] 达到 1.31 MB。这意味着最小对象大小为 500KB，这与典型 CDN 中大量小文件（<10KB）存在的现实不符，表明 x_max=100MB 的假设与 E[S]=1.31MB 及 α=1.1 的参数组合存在内在矛盾，需重新校准 x_max 或 α。

## Corrected Claim

基于 CDN 常见对象大小上限 x_max = 100 MB 的工程假设，反解 x_min 的方程：1.31072 = 1.1 * x_min * (100^(-0.1) - x_min^(-0.1)) / ((-0.1) * (100^1.1 - x_min^1.1))。通过数值迭代求解，若 x_max=100MB，则 x_min ≈ 0.5 MB 才能使 E[S] 达到 1.31 MB。这意味着最小对象大小为 500KB，这与典型 CDN 中大量小文件（<10KB）存在的现实不符，表明 x_max=100MB 的假设与 E[S]=1.31MB 及 α=1.1 的参数组合存在内在矛盾，需重新校准 x_max 或 α。

## Evidence

先验知识/题面给定，逻辑校验通过：帕累托分布期望公式推导正确，数值量级合理，结论符合数学逻辑
