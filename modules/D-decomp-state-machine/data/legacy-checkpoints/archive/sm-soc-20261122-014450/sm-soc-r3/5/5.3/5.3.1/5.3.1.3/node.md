# N293: 若实际有效样本量 n_eff 因数据清洗（如剔除异常值或重复咨询）低于名义值 1000，需计算 n_eff 与 1000 的比值 k，并将标准误放大 sqrt(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

若实际有效样本量 n_eff 因数据清洗（如剔除异常值或重复咨询）低于名义值 1000，需计算 n_eff 与 1000 的比值 k，并将标准误放大 sqrt(1/k) 倍以反映抽样误差的真实膨胀。

## Corrected Claim

若实际有效样本量 n_eff 因数据清洗（如剔除异常值或重复咨询）低于名义值 1000，需计算 n_eff 与 1000 的比值 k，并将标准误放大 sqrt(1/k) 倍以反映抽样误差的真实膨胀。

## Evidence

先验知识/题面给定，逻辑校验通过：标准误与样本量的平方根成反比，有效样本量减少为 k 倍时，标准误放大 sqrt(1/k) 倍符合统计学基本原理。
