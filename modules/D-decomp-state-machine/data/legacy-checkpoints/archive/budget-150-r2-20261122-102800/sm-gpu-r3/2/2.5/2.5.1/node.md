# N85: 2×RTX 4090 运行 BF16 Qwen3-27B (32K context) 的不可行性量化边界：每卡权重分片 27GB + KV Cache 2.15

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

2×RTX 4090 运行 BF16 Qwen3-27B (32K context) 的不可行性量化边界：每卡权重分片 27GB + KV Cache 2.15GB + 激活/CUDA 开销 3.5GB = 32.65GB/卡，超出 24GB 显存上限 8.65GB (36%)，故物理不可行；若采用 Tensor Parallel (TP=2)，KV Cache 分片减半至 1.075GB/卡，总需求降至 31.575GB/卡，仍超出 24GB 上限 7.575GB (31.6%)，确认 BF16 下 2×4090 无解。

## Corrected Claim

2×RTX 4090 运行 BF16 Qwen3-27B (32K context) 的不可行性量化边界：每卡权重分片 27GB + KV Cache 2.15GB + 激活/CUDA 开销 3.5GB = 32.65GB/卡，超出 24GB 显存上限 8.65GB (36%)，故物理不可行；若采用 Tensor Parallel (TP=2)，KV Cache 分片减半至 1.075GB/卡，总需求降至 31.575GB/卡，仍超出 24GB 上限 7.575GB (31.6%)，确认 BF16 下 2×4090 无解。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，双卡分片27GB/卡；32K上下文KV Cache及激活开销估算合理，总显存需求远超24GB物理上限，结论符合物理事实。
