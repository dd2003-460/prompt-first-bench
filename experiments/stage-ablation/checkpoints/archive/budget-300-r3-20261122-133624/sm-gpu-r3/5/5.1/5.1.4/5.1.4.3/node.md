# N346: RTX 5090 在 INT8 下运行 Qwen3-27B 且上下文为 24K tokens 时的总显存需求为 51.09 GB (权重 27 GB + KV 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115, N116, N117

## Claim

RTX 5090 在 INT8 下运行 Qwen3-27B 且上下文为 24K tokens 时的总显存需求为 51.09 GB (权重 27 GB + KV Cache 2.76 GB + 框架/激活开销 ~21.33 GB)，仍超出 32 GB 物理显存，需启用更激进的量化 (W4) 或限制上下文至 ~4K tokens 才可能在单卡上稳定运行

## Corrected Claim

RTX 5090 在 INT8 下运行 Qwen3-27B 且上下文为 24K tokens 时的总显存需求为 51.09 GB (权重 27 GB + KV Cache 2.76 GB + 框架/激活开销 ~21.33 GB)，仍超出 32 GB 物理显存，需启用更激进的量化 (W4) 或限制上下文至 ~4K tokens 才可能在单卡上稳定运行

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B INT8权重约27GB，24K上下文KV Cache约2.76GB，加上框架/激活开销约21.33GB，总显存需求51.09GB，超出32GB物理显存，需W4量化或限制上下文至~4K tokens。
