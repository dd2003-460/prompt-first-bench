# N144: 基于修正后的11.125GB可用显存与12KB/token的FP8 KV开销，单序列理论最大上下文长度上限为 11.125 * 1024^3 / (12 * 1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

基于修正后的11.125GB可用显存与12KB/token的FP8 KV开销，单序列理论最大上下文长度上限为 11.125 * 1024^3 / (12 * 1024) ≈ 970,000 tokens，远超vLLM配置的max_model_len=262,144，表明显存并非限制单序列长度的瓶颈。

## Corrected Claim

基于修正后的11.125GB可用显存与12KB/token的FP8 KV开销，单序列理论最大上下文长度上限为 11.125 * 1024^3 / (12 * 1024) ≈ 970,000 tokens，远超vLLM配置的max_model_len=262,144，表明显存并非限制单序列长度的瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 11.125 * 1024^3 / (12 * 1024) = 11.125 * 1024^2 / 12 ≈ 970,000，数值量级正确，且远大于 262,144，结论自洽。
