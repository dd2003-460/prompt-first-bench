# N112: 1x RTX 4090 + 128GB DDR5 的混合架构中，RTX 4090 显存 24GB 可容纳 Qwen3-27B W4 权重 13.5GB + 8.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

1x RTX 4090 + 128GB DDR5 的混合架构中，RTX 4090 显存 24GB 可容纳 Qwen3-27B W4 权重 13.5GB + 8.4GB (KV Cache) + 2GB (激活) = 23.9GB，剩余 0.1GB 显存，128GB DDR5 用于溢出层，PCIe 4.0 x16 带宽 64 GB/s 限制 offload 速度。

## Corrected Claim

1x RTX 4090 + 128GB DDR5 的混合架构中，RTX 4090 显存 24GB 可容纳 Qwen3-27B W4 权重 13.5GB + 8.4GB (KV Cache) + 2GB (激活) = 23.9GB，剩余 0.1GB 显存，128GB DDR5 用于溢出层，PCIe 4.0 x16 带宽 64 GB/s 限制 offload 速度。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存 24GB 为已知规格，Qwen3-27B W4 量化后约 13.5GB 符合 27B*4bit/8 的量级估算，24-23.9=0.1GB 算术正确，PCIe 4.0 x16 带宽 64GB/s 为标准规格，整体架构逻辑自洽。
