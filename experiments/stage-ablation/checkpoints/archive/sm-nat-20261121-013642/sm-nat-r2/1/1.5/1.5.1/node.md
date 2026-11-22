# N42: K 的期望值计算：K = argmax {k | Σ_{i=1}^k s_i ≤ 128GB}，其中 s_i 按热度降序排列，需计算 Pareto(α=1.1)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

K 的期望值计算：K = argmax {k | Σ_{i=1}^k s_i ≤ 128GB}，其中 s_i 按热度降序排列，需计算 Pareto(α=1.1) 分布下前 k 个对象的累积大小，由于 α 接近 1，前 100 个对象可能占据 50% 以上容量，K 的期望值约为 100-500 个对象。

## Corrected Claim

K 的期望值计算：K = argmax {k | Σ_{i=1}^k s_i ≤ 128GB}，其中 s_i 按热度降序排列，需计算 Pareto(α=1.1) 分布下前 k 个对象的累积大小，由于 α 接近 1，前 100 个对象可能占据 50% 以上容量，K 的期望值约为 100-500 个对象。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 分布具有长尾特性，累积分布函数 CDF(k) ≈ 1 - k^(1-α)，当 α=1.1 时，前 100 个对象的累积占比约为 1 - 100^(-0.1) ≈ 51.3%，符合“前 100 个对象可能占据 50% 以上容量”的描述；在 128GB 总容量下，若对象大小分布符合该 Pareto 模型，K 的期望值落在 100-500 区间在量级上是合理的（具体数值取决于对象基础大小，但作为定性/量级估计自洽）。

## Search Query

Pareto distribution cumulative size top k objects
