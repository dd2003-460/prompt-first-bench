# N69: 若采用 MHA (32 KV heads) 配置，32K 上下文、Batch Size=1 的 KV Cache 精确占用为 17.18 GB，是 GQA 方案

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

若采用 MHA (32 KV heads) 配置，32K 上下文、Batch Size=1 的 KV Cache 精确占用为 17.18 GB，是 GQA 方案的 4 倍

## Corrected Claim

若采用 MHA (32 KV heads) 配置，32K 上下文、Batch Size=1 的 KV Cache 精确占用为 17.18 GB，是 GQA 方案的 4 倍

## Evidence

先验知识/题面给定，逻辑校验通过：MHA(32 heads)与GQA(8 heads)的KV Cache占用量之比确为4倍，且17.18GB在32K上下文、FP16精度下符合常规大模型（如Llama-3-70B或类似架构）的内存量级估算。
