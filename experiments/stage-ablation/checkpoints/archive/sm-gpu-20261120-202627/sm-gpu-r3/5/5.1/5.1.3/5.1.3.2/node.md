# N374: PCIe 4.0 x16 带宽对 KV Cache 传输的瓶颈量化：在 32K 上下文、Batch Size=1 时，每生成 1 token 需读取的 KV C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

PCIe 4.0 x16 带宽对 KV Cache 传输的瓶颈量化：在 32K 上下文、Batch Size=1 时，每生成 1 token 需读取的 KV Cache 字节数 = 2 × 64 (layers) × 4096 (hidden) × 2 (bytes/BF16) × 32768 (seq_len) ≈ 34.4 GB，除以 PCIe 4.0 带宽 32 GB/s，理论最小延迟 ≈ 1.075 秒/token，即理论吞吐量上限 ≈ 0.93 tokens/s (仅考虑 KV 读取，未计计算)，实际因流水线重叠和缓存命中会高于此下限，但远低于 HBM 带宽下的性能。

## Corrected Claim

PCIe 4.0 x16 带宽对 KV Cache 传输的瓶颈量化：在 32K 上下文、Batch Size=1 时，每生成 1 token 需读取的 KV Cache 字节数 = 2 × 64 (layers) × 4096 (hidden) × 2 (bytes/BF16) × 32768 (seq_len) ≈ 34.4 GB，除以 PCIe 4.0 带宽 32 GB/s，理论最小延迟 ≈ 1.075 秒/token，即理论吞吐量上限 ≈ 0.93 tokens/s (仅考虑 KV 读取，未计计算)，实际因流水线重叠和缓存命中会高于此下限，但远低于 HBM 带宽下的性能。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小计算 (2*64*4096*2*32768 ≈ 34.4GB) 及延迟推导 (34.4GB / 32GB/s ≈ 1.075s) 符合算术逻辑与 PCIe 4.0 带宽规格。
