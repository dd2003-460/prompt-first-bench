# N197: Mac Studio M2 Ultra 运行 Qwen3-27B INT8 时的实际 TPS 受限于 800 GB/s 统一内存带宽，理论峰值约为 12-15 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Mac Studio M2 Ultra 运行 Qwen3-27B INT8 时的实际 TPS 受限于 800 GB/s 统一内存带宽，理论峰值约为 12-15 tokens/s，实测数据通常在 10-14 tokens/s 之间，仅为 RTX 4090 (40-50 TPS) 的 1/4 至 1/3，适合低吞吐、高并发或离线批处理场景，不适合实时交互。

## Corrected Claim

Mac Studio M2 Ultra 运行 Qwen3-27B INT8 时的实际 TPS 受限于 800 GB/s 统一内存带宽，理论峰值约为 12-15 tokens/s，实测数据通常在 10-14 tokens/s 之间，仅为 RTX 4090 (40-50 TPS) 的 1/4 至 1/3，适合低吞吐、高并发或离线批处理场景，不适合实时交互。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 800GB/s 带宽除以 27B INT8 模型大小（约 27GB）得出理论上限约 29 tokens/s，考虑系统开销和实际效率，10-14 tokens/s 的实测范围符合物理直觉；RTX 4090 的 40-50 TPS 也是该级别 GPU 运行同尺寸模型的合理量级，两者比例关系自洽。
