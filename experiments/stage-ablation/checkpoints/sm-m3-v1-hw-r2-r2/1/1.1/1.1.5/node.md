# N38: 在 48.5 GB 可用 KV 空间限制下，单个序列的最大可持续缓存 Token 数为 48.5 GB / 8 MB/token ≈ 6144 tokens，而

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

在 48.5 GB 可用 KV 空间限制下，单个序列的最大可持续缓存 Token 数为 48.5 GB / 8 MB/token ≈ 6144 tokens，而非 262,144 tokens，这是硬件决定的硬性并发瓶颈

## Corrected Claim

在 48.5 GB 可用 KV 空间限制下，单个序列的最大可持续缓存 Token 数为 48.5 GB / 8 MB/token ≈ 6144 tokens，而非 262,144 tokens，这是硬件决定的硬性并发瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：48.5GB / 8MB = 6144，计算正确且符合硬件限制逻辑
