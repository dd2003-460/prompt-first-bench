# N149: 在忽略大小-热度相关性时，前 k_max 个对象的总字节量近似公式为 S_total(k_max) ≈ k_max * E[S | rank ≤ k_max]，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

在忽略大小-热度相关性时，前 k_max 个对象的总字节量近似公式为 S_total(k_max) ≈ k_max * E[S | rank ≤ k_max]，用于快速估算 k_max 的初始值，随后需通过精确求和修正。

## Corrected Claim

在忽略大小-热度相关性时，前 k_max 个对象的总字节量近似公式为 S_total(k_max) ≈ k_max * E[S | rank ≤ k_max]，用于快速估算 k_max 的初始值，随后需通过精确求和修正。

## Evidence

先验知识/题面给定，逻辑校验通过
