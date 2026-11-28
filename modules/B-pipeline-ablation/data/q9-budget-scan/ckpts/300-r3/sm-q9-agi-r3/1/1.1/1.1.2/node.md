# N37: 基于 48.5GB 可用内存与 4KB/token 的 KV 开销，单序列最大上下文长度上限为 48.5e9 / 4e3 ≈ 12.1M tokens，远超 m

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

基于 48.5GB 可用内存与 4KB/token 的 KV 开销，单序列最大上下文长度上限为 48.5e9 / 4e3 ≈ 12.1M tokens，远超 max_model_len=262144，故内存非限制因素

## Corrected Claim

基于 48.5GB 可用内存与 4KB/token 的 KV 开销，单序列最大上下文长度上限为 48.5e9 / 4e3 ≈ 12.1M tokens，远超 max_model_len=262144，故内存非限制因素

## Evidence

先验知识/题面给定，逻辑校验通过：48.5GB / 4KB ≈ 12.1M tokens，远大于 262144，结论成立
