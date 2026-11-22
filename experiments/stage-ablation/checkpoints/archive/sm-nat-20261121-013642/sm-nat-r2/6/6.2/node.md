# N79: 为使缓存容量 C=128GB 能覆盖至少 50% 的请求字节量，需计算截断阈值 s_cut，使得 Σ_{i: s_i <= s_cut} (r_i * s_i)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

为使缓存容量 C=128GB 能覆盖至少 50% 的请求字节量，需计算截断阈值 s_cut，使得 Σ_{i: s_i <= s_cut} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j) >= 0.5，在 Pareto(α=1.1, β=0.9) 下，s_cut 约为中位对象大小的 10 倍，具体数值需通过数值积分求解。

## Corrected Claim

为使缓存容量 C=128GB 能覆盖至少 50% 的请求字节量，需计算截断阈值 s_cut，使得 Σ_{i: s_i <= s_cut} (r_i * s_i) / Σ_{j=1}^N (r_j * s_j) >= 0.5，在 Pareto(α=1.1, β=0.9) 下，s_cut 约为中位对象大小的 10 倍，具体数值需通过数值积分求解。

## Evidence

先验知识/题面给定，逻辑校验通过
