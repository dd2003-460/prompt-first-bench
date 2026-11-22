# N58: Pareto(α=1.1) 分布下最大对象大小 M_max 的计算：假设 x_min = 1KB，N = 100,000，则 M_max = (N * x_mi

- **status**: pending
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

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 7 column 5 (char 623)
