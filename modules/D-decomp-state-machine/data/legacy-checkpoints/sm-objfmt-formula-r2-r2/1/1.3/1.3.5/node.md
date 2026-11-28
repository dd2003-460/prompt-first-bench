# N44: 在 Batch Size=1、Seq_Len=32K 的典型推理场景下，vLLM 的激活值内存占用约为 0.5-1GB（4096 × 32768 × 2 byt

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

在 Batch Size=1、Seq_Len=32K 的典型推理场景下，vLLM 的激活值内存占用约为 0.5-1GB（4096 × 32768 × 2 bytes × 1 layer / 1024^3 ≈ 0.25GB，考虑多层缓存和碎片开销后取 0.5-1GB）。

## Corrected Claim

在 Batch Size=1、Seq_Len=32K 的典型推理场景下，vLLM 的激活值内存占用约为 0.5-1GB（4096 × 32768 × 2 bytes × 1 layer / 1024^3 ≈ 0.25GB，考虑多层缓存和碎片开销后取 0.5-1GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：计算基础层激活值约为0.25GB，考虑Transformer多层结构及KV Cache等实际推理开销，0.5-1GB的量级估计符合工程常识。
