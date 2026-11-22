# N374: AMD MI300X 在 ROCm 6.1+ 版本下对 vLLM 的支持已趋于稳定，但针对 Qwen3-27B 的 GQA 架构优化内核（如 FlashAtte

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N132

## Claim

AMD MI300X 在 ROCm 6.1+ 版本下对 vLLM 的支持已趋于稳定，但针对 Qwen3-27B 的 GQA 架构优化内核（如 FlashAttention-3 或 PagedAttention 变体）的实测吞吐量通常比 NVIDIA CUDA 栈低 15-25% [待核验]，该效率损耗系数需作为 MI300X 理论带宽优势的折减因子。

## Corrected Claim

AMD MI300X 在 ROCm 6.1+ 版本下对 vLLM 的支持已趋于稳定，但针对 Qwen3-27B 的 GQA 架构优化内核的实测吞吐量通常低于 NVIDIA CUDA 栈，具体效率损耗需根据实际工作负载实测确定，不宜直接套用固定折减因子。

## Evidence

[质询]具体数值区间（15-25%）缺乏公开基准测试支持，且不同模型规模、序列长度及具体内核实现（FlashAttention-3 vs PagedAttention）下性能差异波动极大，该固定区间可能过于武断或基于特定未公开场景。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能损耗系数属于经验参数，无法从第一性原理推导，故降级）。

## Search Query

AMD MI300X vLLM Qwen3 benchmark throughput comparison CUDA
