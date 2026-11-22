# N44: 不同并发数下的总 KV Cache 显存占用：N=1 时 128 MB, N=4 时 512 MB, N=8 时 1 GB, N=16 时 2 GB (32K 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

不同并发数下的总 KV Cache 显存占用：N=1 时 128 MB, N=4 时 512 MB, N=8 时 1 GB, N=16 时 2 GB (32K 上下文 BF16)

## Corrected Claim

不同并发数下的总 KV Cache 显存占用：N=1 时 128 MB, N=4 时 512 MB, N=8 时 1 GB, N=16 时 2 GB (32K 上下文 BF16)

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 显存占用与并发数 N 呈线性关系（N=1 为 128MB，N=4 为 512MB，N=8 为 1GB，N=16 为 2GB），数值量级与 32K 上下文 BF16 精度下的典型工程估算一致，无内部矛盾。
