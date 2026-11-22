# N340: 在 32K 上下文长度下，H100 的 KV Cache 占用为 12.8GB，加上 54GB 权重后总显存占用 66.8GB，低于 80GB 显存上限，无 S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

在 32K 上下文长度下，H100 的 KV Cache 占用为 12.8GB，加上 54GB 权重后总显存占用 66.8GB，低于 80GB 显存上限，无 Swap 发生

## Corrected Claim

在 32K 上下文长度下，H100 的 KV Cache 占用为 12.8GB，加上 54GB 权重后总显存占用 66.8GB，低于 80GB 显存上限，无 Swap 发生

## Evidence

先验知识/题面给定，逻辑校验通过：12.8GB + 54GB = 66.8GB，且 66.8GB < 80GB，数值计算与逻辑推导自洽。
