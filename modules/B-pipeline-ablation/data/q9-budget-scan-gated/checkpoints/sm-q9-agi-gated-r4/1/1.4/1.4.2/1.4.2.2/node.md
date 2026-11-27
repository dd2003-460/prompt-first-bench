# N50: 修正 N26 错误后，实际可用上下文长度由 KV Cache 显存决定：若可用 KV Cache 为 10.5 GB（N36 修正值），每 token KV 开

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

修正 N26 错误后，实际可用上下文长度由 KV Cache 显存决定：若可用 KV Cache 为 10.5 GB（N36 修正值），每 token KV 开销 12 KB（N20），则最大上下文长度为 10.5 * 1024^3 / 12 * 1024 ≈ 917,504 tokens，但受限于 N18/N21 的矛盾，需优先解决显存分配矛盾以确定真实上限。

## Corrected Claim

修正 N26 错误后，实际可用上下文长度由 KV Cache 显存决定：若可用 KV Cache 为 10.5 GB（N36 修正值），每 token KV 开销 12 KB（N20），则最大上下文长度为 10.5 * 1024^3 / 12 * 1024 ≈ 917,504 tokens，但受限于 N18/N21 的矛盾，需优先解决显存分配矛盾以确定真实上限。

## Evidence

父节点级核验失败（LLM 错误）：curl rc=28 b''
