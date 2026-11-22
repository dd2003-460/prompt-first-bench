# N87: 2×A6000 (96GB total) 运行 BF16 Qwen3-27B 的显存分布与效率：每卡权重分片 27GB + KV Cache 2.15GB + 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

2×A6000 (96GB total) 运行 BF16 Qwen3-27B 的显存分布与效率：每卡权重分片 27GB + KV Cache 2.15GB + 激活/CUDA 3.5GB = 32.65GB/卡，低于 48GB 上限，单卡利用率 68.0%；相比 2×4090 (INT8) 的 75.3% 利用率，A6000 方案显存冗余更大，但避免了多卡间 KV Cache 同步的通信开销，适合对延迟敏感的低并发场景。

## Corrected Claim

2×A6000 (96GB total) 运行 BF16 Qwen3-27B 的显存分布与效率：每卡权重分片 27GB + KV Cache 2.15GB + 激活/CUDA 3.5GB = 32.65GB/卡，低于 48GB 上限，单卡利用率 68.0%；相比 2×4090 (INT8) 的 75.3% 利用率，A6000 方案显存冗余更大，但避免了多卡间 KV Cache 同步的通信开销，适合对延迟敏感的低并发场景。

## Evidence

先验知识/题面给定，逻辑校验通过：27B BF16权重约54GB，双卡分片27GB/卡合理；总显存占用32.65GB低于48GB上限，利用率68%计算正确；A6000 48GB显存大于4090 24GB，冗余更大且避免KV同步开销符合硬件特性。
