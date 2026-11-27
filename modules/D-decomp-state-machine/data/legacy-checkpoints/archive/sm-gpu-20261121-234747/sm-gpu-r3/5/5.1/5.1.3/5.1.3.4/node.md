# N331: 在 32K 上下文长度下，2×RTX 4090 的 KV Cache 分片后每卡占用 6.4GB，加上 27GB 权重后每卡总显存占用 33.4GB，低于 24

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

在 32K 上下文长度下，2×RTX 4090 的 KV Cache 分片后每卡占用 6.4GB，加上 27GB 权重后每卡总显存占用 33.4GB，低于 24GB 显存上限，无 Swap 发生

## Corrected Claim

在 32K 上下文长度下，2×RTX 4090 的 KV Cache 分片后每卡占用 6.4GB，加上 27GB 权重后每卡总显存占用 33.4GB，高于 24GB 显存上限，必然发生 Swap 或 OOM。

## Evidence

[质询]数值逻辑矛盾：27GB 权重 + 6.4GB KV Cache = 33.4GB，该数值明确高于 24GB 显存上限，陈述中却声称“低于 24GB 显存上限”，存在直接的事实与逻辑错误。 | 逻辑校验失败：33.4GB > 24GB，陈述内部数值与结论自相矛盾。
