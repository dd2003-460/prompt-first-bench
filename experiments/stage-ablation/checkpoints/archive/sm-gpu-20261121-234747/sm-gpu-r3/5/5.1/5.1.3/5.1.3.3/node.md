# N330: 在 32K 上下文长度下，L40S 的 KV Cache 占用为 12.8GB，加上 54GB 权重后总显存占用 66.8GB，低于 48GB 显存上限，无 S

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

在 32K 上下文长度下，L40S 的 KV Cache 占用为 12.8GB，加上 54GB 权重后总显存占用 66.8GB，低于 48GB 显存上限，无 Swap 发生

## Corrected Claim

在 32K 上下文长度下，L40S 的 KV Cache 占用为 12.8GB，加上 54GB 权重后总显存占用 66.8GB，高于 48GB 显存上限，必然发生 Swap 或 OOM。

## Evidence

[质询]数值逻辑矛盾：12.8GB (KV Cache) + 54GB (权重) = 66.8GB，该数值明显高于 48GB 的显存上限，陈述中却声称“低于 48GB 显存上限”，存在内部算术矛盾。 | 逻辑校验失败：66.8GB > 48GB，陈述内部数值与结论自相矛盾。
