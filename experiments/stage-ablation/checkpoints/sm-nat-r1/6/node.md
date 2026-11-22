# N30: 在 Pareto(α=1.1) 分布下，前 k% 的对象覆盖了约 1 - (0.01)^(1-1.1) ≈ 79.4% 的总字节量（基于累积分布函数 CDF 推

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 Pareto(α=1.1) 分布下，前 k% 的对象覆盖了约 1 - (0.01)^(1-1.1) ≈ 79.4% 的总字节量（基于累积分布函数 CDF 推导），因此 128GB 缓存若覆盖前 20% 对象，其静态字节命中率理论上限约为 79.4%。

## Corrected Claim

在 Pareto(α=1.1) 分布下，前 k% 的对象覆盖了约 1 - (0.01)^(1-1.1) ≈ 79.4% 的总字节量（基于累积分布函数 CDF 推导），因此 128GB 缓存若覆盖前 20% 对象，其静态字节命中率理论上限约为 79.4%。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Pareto distribution CDF cumulative bytes coverage formula
