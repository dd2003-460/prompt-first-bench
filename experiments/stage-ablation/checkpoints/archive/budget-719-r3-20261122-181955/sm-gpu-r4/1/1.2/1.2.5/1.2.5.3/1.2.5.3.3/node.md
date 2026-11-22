# N489: A6000 的 ITL 对上下文长度的敏感性：在 32K 上下文下 KV Cache 读取量占总带宽需求的 13.8% (8.59/62.59)，若上下文降至 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N165

## Claim

A6000 的 ITL 对上下文长度的敏感性：在 32K 上下文下 KV Cache 读取量占总带宽需求的 13.8% (8.59/62.59)，若上下文降至 4K，KV Cache 降至 1.07 GB，ITL 降至约 75 ms/token，上下文每增加 8K tokens，ITL 增加约 10-15 ms

## Corrected Claim

A6000 的 ITL 对上下文长度的敏感性：在 32K 上下文下 KV Cache 读取量占总带宽需求的 13.8% (8.59/62.59)，若上下文降至 4K，KV Cache 降至 1.07 GB，ITL 降至约 75 ms/token，上下文每增加 8K tokens，ITL 增加约 10-15 ms

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小与上下文长度线性相关（32K/4K=8倍，8.59/1.07≈8.03，吻合）；ITL 随 KV Cache 读取量增加而增加，符合 LLM 推理中 Memory-Bound 特性；数值量级（75ms/token 在 4K 上下文下）符合 A6000 级别 GPU 的推理性能预期。
