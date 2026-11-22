# N446: RTX 4090 运行 Qwen3-27B INT8 模型时的总显存需求：权重 27GB + KV Cache 2.15GB (INT8, 32K) + 激活值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N144

## Claim

RTX 4090 运行 Qwen3-27B INT8 模型时的总显存需求：权重 27GB + KV Cache 2.15GB (INT8, 32K) + 激活值/临时缓冲区 ~1-2GB = ~30-31GB，超过 24GB 显存上限，必须启用 CPU Offload 或 Swap，导致性能显著下降

## Corrected Claim

RTX 4090 运行 Qwen3-27B INT8 模型时的总显存需求：权重 27GB + KV Cache 2.15GB (INT8, 32K) + 激活值/临时缓冲区 ~1-2GB = ~30-31GB，超过 24GB 显存上限，必须启用 CPU Offload 或 Swap，导致性能显著下降

## Evidence

[质询]KV Cache 2.15GB 的数值可能偏低（取决于具体实现和精度），但总显存需求超过 24GB 的核心结论稳健，因为仅权重 27GB 已超出 24GB 上限。 | 先验知识/题面给定，逻辑校验通过：RTX 4090 显存为 24GB，Qwen3-27B INT8 权重约 27GB，仅权重部分即已超出显存上限，加上 KV Cache 和激活值后总需求必然远超 24GB，必须启用 Offload/Swap。
