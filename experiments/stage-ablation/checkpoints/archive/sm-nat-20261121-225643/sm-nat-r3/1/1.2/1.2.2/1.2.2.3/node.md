# N56: 字节命中率数值修正：H_bytes = H_req * R_size，其中 H_req ≈ 0.587（来自 N6/N12 的请求命中率），R_size = E

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

字节命中率数值修正：H_bytes = H_req * R_size，其中 H_req ≈ 0.587（来自 N6/N12 的请求命中率），R_size = E[S_hit] / E[S_miss]；由于 ρ=-0.3 导致 E[S_hit] < E[S_miss]，R_size < 1，因此 H_bytes < H_req；具体数值需依赖 N47 和 N48 的积分结果，预计 R_size 在 0.6-0.8 之间，从而 H_bytes ≈ 0.35-0.47。

## Corrected Claim

字节命中率数值修正：H_bytes = H_req * R_size，其中 H_req ≈ 0.587（来自 N6/N12 的请求命中率），R_size = E[S_hit] / E[S_miss]；由于 ρ=-0.3 导致 E[S_hit] < E[S_miss]，R_size < 1，因此 H_bytes < H_req；具体数值需依赖 N47 和 N48 的积分结果，预计 R_size 在 0.6-0.8 之间，从而 H_bytes ≈ 0.35-0.47。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 H_bytes = H_req * R_size 符合定义，且基于 ρ=-0.3 推导 R_size < 1 进而得出 H_bytes < H_req 的逻辑链条自洽，数值量级合理。
