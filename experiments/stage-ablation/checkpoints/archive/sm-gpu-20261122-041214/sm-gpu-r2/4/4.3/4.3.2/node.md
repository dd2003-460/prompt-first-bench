# N130: 修正 KV Cache 单 token 占用计算：基于 N49 确认的参数，每 1K token 单 batch 的 KV Cache 占用 = (2 * 48

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

修正 KV Cache 单 token 占用计算：基于 N49 确认的参数，每 1K token 单 batch 的 KV Cache 占用 = (2 * 48 * 8 * 128 * 2 bytes * 1024) / 1024^3 ≈ 0.15 GB (BF16)，若使用 FP8 量化 KV Cache，该值减半为 0.075 GB/1K token。

## Corrected Claim

修正 KV Cache 单 token 占用计算：基于 N49 确认的参数，每 1K token 单 batch 的 KV Cache 占用 = (2 * 48 * 8 * 128 * 2 bytes * 1024) / 1024^3 ≈ 0.15 GB (BF16)，若使用 FP8 量化 KV Cache，该值减半为 0.075 GB/1K token。

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 (2 * 48 * 8 * 128 * 2 * 1024) / 1024^3 ≈ 0.149 GB，与陈述一致；FP8 减半逻辑正确。
