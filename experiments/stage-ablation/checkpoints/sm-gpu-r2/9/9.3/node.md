# N161: ROCm 软件栈对 Qwen3-27B 的支持存在潜在性能损耗：相比 NVIDIA CUDA 生态，ROCm 的算子优化成熟度较低，可能导致实际吞吐量仅为理论峰

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

ROCm 软件栈对 Qwen3-27B 的支持存在潜在性能损耗：相比 NVIDIA CUDA 生态，ROCm 的算子优化成熟度较低，可能导致实际吞吐量仅为理论峰值的 70-85% [待核验]，需通过 llama.cpp 或 vLLM 在 ROCm 上的具体基准测试数据确认。

## Corrected Claim

ROCm 软件栈对 Qwen3-27B 的支持存在潜在性能损耗：相比 NVIDIA CUDA 生态，ROCm 的算子优化成熟度较低，可能导致实际吞吐量低于理论峰值，具体损耗比例需通过 llama.cpp 或 vLLM 在 ROCm 上的基准测试数据确认。

## Evidence

[质询]70-85% 的具体数值范围缺乏公开基准测试支持，属于经验性估计，不同算子（如 GEMM, Attention）和模型规模下差异巨大，直接断言该区间可能不准确。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能损耗比例无法从第一性原理严格推出）。

## Search Query

Qwen3-27B AMD MI300X ROCm inference benchmark tokens per second
