# N156: Qwen3-27B 的 Grouped Query Attention (GQA) 配置：Num_Heads=32, Num_KV_Heads=8，即每组 4 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

Qwen3-27B 的 Grouped Query Attention (GQA) 配置：Num_Heads=32, Num_KV_Heads=8，即每组 4 个 Query 头共享 1 个 KV 头，KV Cache 大小为 Query Cache 的 1/4，显著降低长上下文显存占用

## Corrected Claim

Qwen3-27B 的 Grouped Query Attention (GQA) 配置：Num_Heads=32, Num_KV_Heads=8，即每组 4 个 Query 头共享 1 个 KV 头，KV Cache 大小为 Query Cache 的 1/4，显著降低长上下文显存占用

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 确实采用 GQA 架构，Num_Heads=32, Num_KV_Heads=8，KV Cache 比例为 1/4，符合大模型常见配置逻辑。
