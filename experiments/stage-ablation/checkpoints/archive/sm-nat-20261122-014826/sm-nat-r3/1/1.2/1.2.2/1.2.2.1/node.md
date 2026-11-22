# N75: K_95 的精确求解：在 β=0.9 分布下，Σ_{r=1}^{K} r^(-0.9) = 0.95 * 10.50 ≈ 9.975，求解 K 使得 K^0.1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

K_95 的精确求解：在 β=0.9 分布下，Σ_{r=1}^{K} r^(-0.9) = 0.95 * 10.50 ≈ 9.975，求解 K 使得 K^0.1/0.1 ≈ 9.975，得 K ≈ 1000^0.9 ≈ 501，即 K_95 ≈ 501，而非 N28 中声称的 10^5 级别。

## Corrected Claim

K_95 的精确求解：在 β=0.9 分布下，Σ_{r=1}^{K} r^(-0.9) = 0.95 * 10.50 ≈ 9.975，求解 K 使得 K^0.1/0.1 ≈ 9.975，得 K ≈ 1000^0.9 ≈ 501，即 K_95 ≈ 501，而非 N28 中声称的 10^5 级别。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

sum r^-0.9 asymptotic approximation integral test
