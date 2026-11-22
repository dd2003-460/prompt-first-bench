# N212: RTX 5090 (32GB) 在 INT8 下运行 Qwen3-27B 的总显存需求：权重 13.5GB + KV Cache (32K上下文, batch=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

RTX 5090 (32GB) 在 INT8 下运行 Qwen3-27B 的总显存需求：权重 13.5GB + KV Cache (32K上下文, batch=1, 约4GB) + 框架/激活开销 (约2-4GB) = 19.5-21.5GB，低于 32GB 物理显存，故单卡 INT8 部署可行，无需 PagedAttention 强制截断上下文。

## Corrected Claim

RTX 5090 (32GB) 在 INT8 下运行 Qwen3-27B 的总显存需求：权重 13.5GB + KV Cache (32K上下文, batch=1, 约4GB) + 框架/激活开销 (约2-4GB) = 19.5-21.5GB，低于 32GB 物理显存，故单卡 INT8 部署可行，无需 PagedAttention 强制截断上下文。

## Evidence

[质询]KV Cache 估算可能偏低：Qwen3-27B 若采用 GQA（如 8 KV heads），32K 上下文下 KV Cache 约为 2.1GB；若采用 MHA（如 32 KV heads），则约为 8.4GB。陈述中“约4GB”处于两者之间，可能隐含了特定的 GQA 配置或量化 KV Cache，若模型实际为 MHA 且未量化 KV，总显存可能接近 25-27GB，虽仍低于 32GB，但余量较小。 | 先验知识/题面给定，逻辑校验通过：INT8 权重 13.5GB 符合 27B 参数规模；KV Cache 与激活开销估算在合理工程范围内；总显存 19.5-21.5GB 低于 32GB 物理显存，单卡部署可行结论成立。
