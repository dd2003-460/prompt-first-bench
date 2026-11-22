# N450: RTX 3090 运行 Qwen3-27B INT8 模型时的总显存需求：权重 27GB + KV Cache 2.15GB (INT8, 32K) + 激活值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N145

## Claim

RTX 3090 运行 Qwen3-27B INT8 模型时的总显存需求：权重 27GB + KV Cache 2.15GB (INT8, 32K) + 激活值/临时缓冲区 ~1-2GB = ~30-31GB，超过 24GB 显存上限，必须启用 CPU Offload 或 Swap，导致性能显著下降

## Corrected Claim

RTX 3090 运行 Qwen3-27B INT8 模型时的总显存需求：权重 27GB + KV Cache 2.15GB (INT8, 32K) + 激活值/临时缓冲区 ~1-2GB = ~30-31GB，超过 24GB 显存上限，必须启用 CPU Offload 或 Swap，导致性能显著下降

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数INT8权重约27GB，加上KV Cache和激活值，总显存需求确实超过24GB，需启用CPU Offload。
