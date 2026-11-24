# N512: 分片存储策略下的带宽消耗模型：将 s_vid 拆分为 N_chunks 个 1MB 分片，并行下载时 T_transfer_parallel = max(T_c

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N172

## Claim

分片存储策略下的带宽消耗模型：将 s_vid 拆分为 N_chunks 个 1MB 分片，并行下载时 T_transfer_parallel = max(T_chunk_i)，若采用 4 路并行，T_transfer ≈ s_vid / (4 × Bandwidth_link)，但需增加 N_chunks 次 HTTP 请求头开销（约 0.5ms/请求），总延迟 T_total = T_transfer_parallel + N_chunks × 0.5ms

## Corrected Claim

分片存储策略下的带宽消耗模型：将 s_vid 拆分为 N_chunks 个 1MB 分片，并行下载时 T_transfer_parallel = max(T_chunk_i)，若采用 4 路并行，T_transfer ≈ s_vid / (4 × Bandwidth_link)，但需增加 N_chunks 次 HTTP 请求头开销（约 0.5ms/请求），总延迟 T_total = T_transfer_parallel + N_chunks × 0.5ms

## Evidence

先验知识/题面给定，逻辑校验通过
