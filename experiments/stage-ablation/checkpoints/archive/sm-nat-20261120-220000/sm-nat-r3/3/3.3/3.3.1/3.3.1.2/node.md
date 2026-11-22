# N114: S_max=10MB 截断对总大小 S_total 的影响量化：S_total = N * S_min * (1 - (S_max/S_min)^{-(α-1)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

S_max=10MB 截断对总大小 S_total 的影响量化：S_total = N * S_min * (1 - (S_max/S_min)^{-(α-1)})/(α-1)，代入 N=100,000, S_min=1KB, S_max=10MB (10,000KB), α=1.1，得 S_total ≈ 100,000 * 1KB * (1 - 10000^{-0.1})/0.1 ≈ 100,000 * 1KB * 6.31 ≈ 631 MB，远小于 128GB 缓存，确认 C >> S_total 假设成立。

## Corrected Claim

S_max=10MB 截断对总大小 S_total 的影响量化：S_total = N * S_min * (1 - (S_max/S_min)^{-(α-1)})/(α-1)，代入 N=100,000, S_min=1KB, S_max=10MB (10,000KB), α=1.1，得 S_total ≈ 100,000 * 1KB * (1 - 10000^{-0.1})/0.1 ≈ 100,000 * 1KB * 6.31 ≈ 631 MB，远小于 128GB 缓存，确认 C >> S_total 假设成立。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Pareto distribution truncated mean formula S_max S_min alpha
