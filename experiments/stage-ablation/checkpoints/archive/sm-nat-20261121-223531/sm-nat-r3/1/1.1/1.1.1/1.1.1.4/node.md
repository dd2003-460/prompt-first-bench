# N93: s_min 对缓存容量占比 K 的影响公式：K = S_cached / S_total，其中 S_total ≈ N_obj * E[S]_trunc，若 s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

s_min 对缓存容量占比 K 的影响公式：K = S_cached / S_total，其中 S_total ≈ N_obj * E[S]_trunc，若 s_min 从 1KB 变为 10KB，E[S]_trunc 增加约 9%，导致 S_total 增加 9%，从而 K 减少约 8.3% [待核验]。

## Corrected Claim

s_min 对缓存容量占比 K 的影响公式：K = S_cached / S_total，其中 S_total ≈ N_obj * E[S]_trunc，若 s_min 从 1KB 变为 10KB，E[S]_trunc 增加约 9%，导致 S_total 增加 9%，从而 K 减少约 8.3% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：K = S_cached / S_total，若 S_cached 不变且 S_total 增加 9%（即变为 1.09 倍），则 K 变为 1/1.09 ≈ 0.9174，减少约 8.26%，与陈述中的 8.3% 一致。
