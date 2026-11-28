# N107: Qwen3-27B 的 num_key_value_heads=8 (GQA) 将 KV Cache 大小缩减至 MHA (num_attention_head

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Qwen3-27B 的 num_key_value_heads=8 (GQA) 将 KV Cache 大小缩减至 MHA (num_attention_heads=32) 的 1/4，若为 MHA 架构，32K 上下文 KV Cache 将达 68.72 GB，GQA 是 24GB/48GB 显卡能运行 32K 上下文的关键架构特征。

## Corrected Claim

Qwen3-27B 的 num_key_value_heads=8 (GQA) 将 KV Cache 大小缩减至 MHA (num_attention_heads=32) 的 1/4，若为 MHA 架构，32K 上下文 KV Cache 将达 68.72 GB，GQA 是 24GB/48GB 显卡能运行 32K 上下文的关键架构特征。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 采用 GQA 架构，KV 头数为 8，注意力头数为 32，比例确为 1/4；32K 上下文下 MHA 的 KV Cache 约为 68.72 GB，GQA 将其缩减至约 17.18 GB，符合 24GB/48GB 显卡运行需求。
