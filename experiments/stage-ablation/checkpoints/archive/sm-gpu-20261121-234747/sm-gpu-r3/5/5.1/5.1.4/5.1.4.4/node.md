# N341: 在 32K 上下文长度下，2×A100 的 KV Cache 分片后每卡占用 6.4GB，加上 27GB 权重后每卡总显存占用 33.4GB，低于 40GB 显

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

在 32K 上下文长度下，2×A100 的 KV Cache 分片后每卡占用 6.4GB，加上 27GB 权重后每卡总显存占用 33.4GB，低于 40GB 显存上限，无 Swap 发生

## Corrected Claim

在 32K 上下文长度下，2×A100 的 KV Cache 分片后每卡占用 6.4GB，加上 27GB 权重后每卡总显存占用 33.4GB，低于 40GB 显存上限，无 Swap 发生

## Evidence

先验知识/题面给定，逻辑校验通过：6.4GB + 27GB = 33.4GB < 40GB，算术自洽且符合显存占用逻辑
