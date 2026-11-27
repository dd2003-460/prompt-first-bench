# N256: NVFP4 反量化到 FP16 的额外计算开销（Dequantization Overhead）约为 5-10% 的 GPU 周期，主要消耗在 CUDA Cor

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

NVFP4 反量化到 FP16 的额外计算开销（Dequantization Overhead）约为 5-10% 的 GPU 周期，主要消耗在 CUDA Core 而非 Tensor Core 上，导致整体 GEMM 吞吐量下降至 FP16 峰值的 90-95%，而非 N94 声称的 60-70%。

## Corrected Claim

NVFP4 反量化到 FP16 的额外计算开销通常较低（约 5-10% GPU 周期），主要消耗在 CUDA Core 上，使得整体 GEMM 吞吐量接近 FP16 峰值（约 90-95%），具体数值取决于硬件架构与实现优化。

## Evidence

[质询]具体数值（5-10% 开销、90-95% 吞吐量）属于特定硬件架构和实现细节下的经验数据，缺乏通用性，且不同 GPU 架构（如 Hopper vs Blackwell）及软件栈优化程度会导致显著差异，无法作为绝对事实。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 NVFP4 dequantization overhead vLLM benchmark
