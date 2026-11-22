# N19: BF16全精度下Qwen3-27B的显存占用为54GB（27B参数 × 2 bytes/param），推理时KV Cache开销随上下文长度线性增长，32K上下

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

BF16全精度下Qwen3-27B的显存占用为54GB（27B参数 × 2 bytes/param），推理时KV Cache开销随上下文长度线性增长，32K上下文下KV Cache约占用4-8GB（取决于层数和head数）

## Corrected Claim

BF16全精度下Qwen3-27B的显存占用为54GB（27B参数 × 2 bytes/param），推理时KV Cache开销随上下文长度线性增长，32K上下文下KV Cache约占用4-8GB（取决于层数和head数）

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数×2字节=54GB权重显存计算正确；KV Cache随上下文线性增长符合Transformer架构原理，32K上下文下4-8GB的量级估算在合理范围内（取决于具体模型配置如层数、头数、GQA比例等）。
