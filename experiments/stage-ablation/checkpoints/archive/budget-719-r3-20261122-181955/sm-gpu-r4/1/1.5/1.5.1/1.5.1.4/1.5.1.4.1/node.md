# N577: Apple M1 Max 在 Qwen3-27B INT4 量化下的权重文件大小为 13.5 GB (27B params * 0.5 bytes/param)

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N200

## Claim

Apple M1 Max 在 Qwen3-27B INT4 量化下的权重文件大小为 13.5 GB (27B params * 0.5 bytes/param)，这是其在 64GB 统一内存下运行的必要前提。

## Corrected Claim

Apple M1 Max 在 Qwen3-27B INT4 量化下的权重文件大小为 13.5 GB (27B params * 0.5 bytes/param)，这是其在 64GB 统一内存下运行的必要前提。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 0.5 bytes/param (INT4) = 13.5 GB，计算正确且符合M1 Max 64GB内存运行该模型的常识。
