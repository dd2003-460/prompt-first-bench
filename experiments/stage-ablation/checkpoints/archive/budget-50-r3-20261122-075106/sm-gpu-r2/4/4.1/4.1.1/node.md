# N74: RTX 4090 运行 Qwen3-27B (BF16) 时，由于 54GB 权重 > 24GB 显存，必须启用 CPU Offload 或量化，若使用 CPU

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

RTX 4090 运行 Qwen3-27B (BF16) 时，由于 54GB 权重 > 24GB 显存，必须启用 CPU Offload 或量化，若使用 CPU Offload，内存带宽瓶颈将主导性能，DRAM 带宽通常为 50-100 GB/s

## Corrected Claim

RTX 4090 运行 Qwen3-27B (BF16) 时，由于 54GB 权重 > 24GB 显存，必须启用 CPU Offload 或量化，若使用 CPU Offload，内存带宽瓶颈将主导性能，DRAM 带宽通常为 50-100 GB/s

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，超过RTX 4090的24GB显存，必须启用CPU Offload或量化；CPU Offload时DRAM带宽（50-100 GB/s）远低于GPU显存带宽，成为性能瓶颈，符合基本硬件原理。
