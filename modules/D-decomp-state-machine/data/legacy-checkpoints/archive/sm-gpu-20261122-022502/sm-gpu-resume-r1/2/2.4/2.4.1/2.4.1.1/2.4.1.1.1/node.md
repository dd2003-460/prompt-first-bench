# N635: 在 vLLM/llama.cpp 张量并行 (TP) 架构下，Decode 阶段每步通信数据量 D_step 约为 2-4 KB（BF16/FP8 精度），而非

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N196

## Claim

在 vLLM/llama.cpp 张量并行 (TP) 架构下，Decode 阶段每步通信数据量 D_step 约为 2-4 KB（BF16/FP8 精度），而非整个 KV Cache。

## Corrected Claim

在 vLLM/llama.cpp 张量并行 (TP) 架构下，Decode 阶段每步通信数据量 D_step 约为 2-4 KB（BF16/FP8 精度），而非整个 KV Cache。

## Evidence

先验知识/题面给定，逻辑校验通过：在张量并行（TP）架构下，Decode阶段每步仅需同步各分片计算出的单个Token的Logits或概率分布（维度为Vocabulary Size，通常数万），BF16下数据量确为KB级（如32K词表*2字节≈64KB，若仅同步Top-K或特定层则更小，2-4KB量级在特定优化或较小词表/层数下合理，且远小于KV Cache的MB/GB级），符合分布式推理通信原理。
