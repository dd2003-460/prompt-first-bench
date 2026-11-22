# N17: 生成速度（Tokens per Second, TPS）的主要决定因素是 KV Cache 读写带宽和矩阵乘法算力，公式：TPS ≈ min(Memory_Ba

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

生成速度（Tokens per Second, TPS）的主要决定因素是 KV Cache 读写带宽和矩阵乘法算力，公式：TPS ≈ min(Memory_Bandwidth / KV_Cache_Size_Per_Token, Compute_Throughput / FLOPs_Per_Token)。

## Corrected Claim

生成速度（Tokens per Second, TPS）的主要决定因素是 KV Cache 读写带宽和矩阵乘法算力，公式：TPS ≈ min(Memory_Bandwidth / KV_Cache_Size_Per_Token, Compute_Throughput / FLOPs_Per_Token)。

## Evidence

先验知识/题面给定，逻辑校验通过：LLM推理中，自回归生成阶段主要受限于KV Cache的内存带宽（Memory Bound）和矩阵乘法的计算能力（Compute Bound），TPS由两者瓶颈中的较小值决定，符合Roofline模型及大模型推理的基本原理。
