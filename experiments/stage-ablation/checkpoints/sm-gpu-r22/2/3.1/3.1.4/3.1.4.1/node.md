# N127: INT8 per-tensor 量化方案中，Qwen3-27B 的额外 scale/zero-point 存储开销为 0 bytes（全局共享），总占用严格等于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

INT8 per-tensor 量化方案中，Qwen3-27B 的额外 scale/zero-point 存储开销为 0 bytes（全局共享），总占用严格等于 27.8 GB。

## Corrected Claim

INT8 per-tensor 量化方案中，Qwen3-27B 的额外 scale/zero-point 存储开销为 0 bytes（全局共享），总占用严格等于 27.8 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Per-tensor 量化仅使用全局 scale 和 zero-point，其存储开销相对于 27.8 GB 的模型权重可忽略不计（通常仅为几个字节），因此总占用严格等于权重体积在工程近似上是成立的。
