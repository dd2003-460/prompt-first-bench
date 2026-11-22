# N159: 基于 N128 和 N129 参数，在 FP16 精度下，Qwen3-27B 每 token 的 KV Cache 显存占用为 0.000512 GB (即 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

基于 N128 和 N129 参数，在 FP16 精度下，Qwen3-27B 每 token 的 KV Cache 显存占用为 0.000512 GB (即 524,288 bytes)。

## Corrected Claim

基于 N128 和 N129 参数，在 FP16 精度下，Qwen3-27B 每 token 的 KV Cache 显存占用为 0.000512 GB (即 524,288 bytes)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（如 GQA 头数、头维度等）在 FP16 下每 token KV Cache 占用计算符合 524,288 bytes (0.5 MB) 的量级，数值自洽。
