# N158: R_bytes（总字节请求速率）的计算：R_bytes = R_requests * E[S]，其中 R_requests = 50,000,000/day，E

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

R_bytes（总字节请求速率）的计算：R_bytes = R_requests * E[S]，其中 R_requests = 50,000,000/day，E[S] 由 N92 确定（假设 E[S] ≈ 10KB 基于 Pareto α=1.1, s_min=1KB 截断），则 R_bytes ≈ 500,000,000 KB/day ≈ 476.8 GB/day。

## Corrected Claim

R_bytes（总字节请求速率）的计算：R_bytes = R_requests * E[S]，其中 R_requests = 50,000,000/day，E[S] 由 N92 确定（假设 E[S] ≈ 10KB 基于 Pareto α=1.1, s_min=1KB 截断），则 R_bytes ≈ 500,000,000 KB/day ≈ 476.8 GB/day。

## Evidence

先验知识/题面给定，逻辑校验通过：50,000,000 * 10 KB = 500,000,000 KB，换算为 GB (500,000,000 / 1024 / 1024 ≈ 476.836) 与陈述一致，数值量级合理。
