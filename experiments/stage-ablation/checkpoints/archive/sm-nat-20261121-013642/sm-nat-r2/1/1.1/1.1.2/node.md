# N32: 归一化常数推导：若将 100,000 个对象的总大小归一化为 C_total，则单个对象大小的归一化系数 k_size = C_total / Σ_{i=1}^

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

归一化常数推导：若将 100,000 个对象的总大小归一化为 C_total，则单个对象大小的归一化系数 k_size = C_total / Σ_{i=1}^{100,000} x_i，其中 x_i 为未归一化的 Pareto 采样值，需确保 k_size * max(x_i) < 128GB/100,000 以验证平均大小约束。

## Corrected Claim

归一化常数推导：若将 100,000 个对象的总大小归一化为 C_total，则单个对象大小的归一化系数 k_size = C_total / Σ_{i=1}^{100,000} x_i，其中 x_i 为未归一化的 Pareto 采样值，需确保 k_size * max(x_i) < 128GB/100,000 以验证平均大小约束。

## Evidence

先验知识/题面给定，逻辑校验通过：归一化系数定义符合线性缩放原理，约束条件量纲一致且逻辑自洽。
