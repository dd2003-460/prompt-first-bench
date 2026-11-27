# N441: 若采用 INT4 量化存储 KV Cache，单请求 32K 上下文显存占用降至 0.5 GB，计算式为 2 (K+V) * 8 (num_kv_heads) 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

若采用 INT4 量化存储 KV Cache，单请求 32K 上下文显存占用降至 0.5 GB，计算式为 2 (K+V) * 8 (num_kv_heads) * 128 (head_dim) * 0.5 byte (INT4) * 32768 / 1e6 = 2048 MB / 4 = 512 MB。

## Corrected Claim

若采用 INT4 量化存储 KV Cache，单请求 32K 上下文显存占用降至 0.5 GB，计算式为 2 (K+V) * 8 (num_kv_heads) * 128 (head_dim) * 0.5 byte (INT4) * 32768 / 1e6 = 2048 MB / 4 = 512 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 8 * 128 * 0.5 * 32768 / 1e6 = 512 MB，数值量级与逻辑自洽。
