# N33: 适用前提条件：负载特性约束。推荐方案仅在特定负载下成立：(1) 并发请求数 N_concurrent ≤ N_gpus × Batch_Size_Max，若超出

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

适用前提条件：负载特性约束。推荐方案仅在特定负载下成立：(1) 并发请求数 N_concurrent ≤ N_gpus × Batch_Size_Max，若超出则需增加 GPU 或降低 Batch Size 导致效率下降；(2) 上下文长度分布：若 80% 请求 < 4K tokens，则显存带宽瓶颈主导，高带宽卡（如 H100）优势扩大；若 80% 请求 > 16K tokens，则显存容量瓶颈主导，高容量卡（如 A100 80G）优势扩大。需量化不同上下文分布下的最优卡型切换点。

## Corrected Claim

适用前提条件：负载特性约束。推荐方案仅在特定负载下成立：(1) 并发请求数 N_concurrent ≤ N_gpus × Batch_Size_Max，若超出则需增加 GPU 或降低 Batch Size 导致效率下降；(2) 上下文长度分布：若 80% 请求 < 4K tokens，则显存带宽瓶颈主导，高带宽卡（如 H100）优势扩大；若 80% 请求 > 16K tokens，则显存容量瓶颈主导，高容量卡（如 A100 80G）优势扩大。需量化不同上下文分布下的最优卡型切换点。

## Evidence

先验知识/题面给定，逻辑校验通过：并发约束符合GPU并行处理的基本容量限制；上下文长度对显存带宽与容量的影响符合LLM推理中KV Cache占用显存且计算/访存比随序列长度变化的物理直觉。
