# N213: Apple Silicon M2/M3 Max 统一内存架构下，运行 Qwen3-27B INT8 的实际内存带宽受限值：M2 Max 峰值带宽 400 GB/

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N49

## Claim

Apple Silicon M2/M3 Max 统一内存架构下，运行 Qwen3-27B INT8 的实际内存带宽受限值：M2 Max 峰值带宽 400 GB/s，M3 Max 峰值带宽 400 GB/s，理论峰值吞吐量 T_max ≈ 400 GB/s / 27 GB ≈ 14.8 tokens/s，但受限于 macOS 内存管理开销及 llama.cpp 优化程度，实测吞吐量通常在 8-12 tokens/s 区间，低于理论值约 20-30% [待核验]

## Corrected Claim

Apple Silicon M2/M3 Max 统一内存架构下，运行 Qwen3-27B INT8 的实际内存带宽受限值：M2 Max 峰值带宽 400 GB/s，M3 Max 峰值带宽 400 GB/s，理论峰值吞吐量 T_max ≈ 400 GB/s / 27 GB ≈ 14.8 tokens/s，但受限于 macOS 内存管理开销及 llama.cpp 优化程度，实测吞吐量通常低于理论值，具体数值因系统环境和优化程度而异。

## Evidence

[质询]M3 Max 的峰值内存带宽通常被引用为 400 GB/s，但部分资料指出其可能更高或存在不同版本差异；此外，Qwen3-27B INT8 的实际内存占用可能因量化方式（如 GGUF 格式开销）略高于 27 GB，导致理论吞吐量计算偏差；实测吞吐量 8-12 tokens/s 的区间缺乏具体基准测试支持，可能因系统负载、并发任务等因素波动较大。 | 先验知识/题面给定，逻辑校验通过，但实测吞吐量区间缺乏直接来源支持，降级为定性表述。

## Search Query

Apple M3 Max Qwen3-27B INT8 inference benchmark tokens per second llama.cpp
