# N114: Top 10 对象贡献的字节命中率占比 H_top10 的精确公式为 H_top10 = (Σ_{i=1}^{10} λ_i * s_i) / R_total_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

Top 10 对象贡献的字节命中率占比 H_top10 的精确公式为 H_top10 = (Σ_{i=1}^{10} λ_i * s_i) / R_total_bytes，其中 R_total_bytes = 50,000,000 * E[s]_truncated，由于 Top 10 对象大小极小（约 1-10KB），其字节占比远低于其请求占比（5.4%），实际 H_top10 ≈ 0.005-0.02，而非 15%

## Corrected Claim

Top 10 对象贡献的字节命中率占比 H_top10 的精确公式为 H_top10 = (Σ_{i=1}^{10} λ_i * s_i) / R_total_bytes，其中 R_total_bytes = 50,000,000 * E[s]_truncated，由于 Top 10 对象大小极小（约 1-10KB），其字节占比远低于其请求占比（5.4%），实际 H_top10 ≈ 0.005-0.02，而非 15%

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合加权平均逻辑，且基于Top 10对象大小（KB级）远小于平均对象大小（MB级）的常识，推导出的字节占比（0.5%-2%）远低于请求占比（5.4%）在量级上合理且自洽。
