# N752: 基于修正单 token 值 (64 KB) 的 32K 上下文 FP8 KV Cache 总占用：64 KB * 32,768 = 2,097,152 KB =

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N267

## Claim

基于修正单 token 值 (64 KB) 的 32K 上下文 FP8 KV Cache 总占用：64 KB * 32,768 = 2,097,152 KB = 2.0 GB。修正 N267 中 2.147 GB 的计算误差（二进制精确值为 2.0 GiB）。

## Corrected Claim

基于修正单 token 值 (64 KB) 的 32K 上下文 FP8 KV Cache 总占用：64 KB * 32,768 = 2,097,152 KB = 2.0 GB。修正 N267 中 2.147 GB 的计算误差（二进制精确值为 2.0 GiB）。

## Evidence

先验知识/题面给定，逻辑校验通过：64 KB * 32,768 = 2,097,152 KB，换算为 GiB 即 2.0 GiB，计算准确且符合二进制单位定义。
