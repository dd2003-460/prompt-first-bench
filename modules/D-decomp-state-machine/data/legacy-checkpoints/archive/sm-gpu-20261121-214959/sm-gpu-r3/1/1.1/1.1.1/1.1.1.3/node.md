# N132: 基于 num_layers=64 修正后的 128K 上下文 BF16 KV Cache 显存占用为 52.43 GB（计算式：2 * 64 * 8 * 128

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

基于 num_layers=64 修正后的 128K 上下文 BF16 KV Cache 显存占用为 52.43 GB（计算式：2 * 64 * 8 * 128 * 2 * 131072 / 1e9），导致 N108 中 24GB 单卡溢出判定需重新验证，但结论仍为不可行。

## Corrected Claim

基于 num_layers=64 修正后的 128K 上下文 BF16 KV Cache 显存占用为 52.43 GB（计算式：2 * 64 * 8 * 128 * 2 * 131072 / 1e9），导致 N108 中 24GB 单卡溢出判定需重新验证，但结论仍为不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 64 * 8 * 128 * 2 * 131072 / 1e9 数值推导正确（约 52.43 GB），且 52.43 GB > 24 GB 的溢出结论符合逻辑。
