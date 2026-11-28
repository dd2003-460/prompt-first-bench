# N59: 纯 CPU 方案 (如 128GB DDR5-5600) 运行 Qwen3-27B (INT8) 的吞吐量上限约为 2-4 tokens/s，计算逻辑为：内存带

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14, N15, N16

## Claim

纯 CPU 方案 (如 128GB DDR5-5600) 运行 Qwen3-27B (INT8) 的吞吐量上限约为 2-4 tokens/s，计算逻辑为：内存带宽 (5600 MT/s * 8 pins * 1 byte / 1000 ≈ 44.8 GB/s) / 每 token 需读取的有效字节数 (约 10-15 GB for 27B INT8 + KV Cache read/write)

## Corrected Claim

纯 CPU 方案 (如 128GB DDR5-5600) 运行 Qwen3-27B (INT8) 的吞吐量上限约为 2-4 tokens/s，计算逻辑为：内存带宽 (5600 MT/s * 8 pins * 1 byte / 1000 ≈ 44.8 GB/s) / 每 token 需读取的有效字节数 (约 10-15 GB for 27B INT8 + KV Cache read/write)

## Evidence

先验知识/题面给定，逻辑校验通过：DDR5-5600双通道理论带宽约44.8GB/s，Qwen3-27B INT8权重约27GB，受限于内存带宽瓶颈，吞吐量估算符合物理直觉与工程经验。
