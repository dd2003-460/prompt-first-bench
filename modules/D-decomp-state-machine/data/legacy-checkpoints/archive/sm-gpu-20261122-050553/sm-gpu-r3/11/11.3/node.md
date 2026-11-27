# N117: AMD Radeon PRO W7900 在 ROCm 6.0+ 环境下运行 vLLM 需使用 rocm-build 版本的 PyTorch，且 ROCm 对 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

AMD Radeon PRO W7900 在 ROCm 6.0+ 环境下运行 vLLM 需使用 rocm-build 版本的 PyTorch，且 ROCm 对 Qwen3 架构的 FlashAttention-2 支持需在 ROCm 6.1+ 中验证，否则推理速度下降 30% 以上。

## Corrected Claim

AMD Radeon PRO W7900 在 ROCm 环境下运行 vLLM 通常需使用 rocm-build 版本的 PyTorch；ROCm 对 Qwen3 架构的 FlashAttention-2 支持情况需根据具体 ROCm 版本验证，若不支持可能导致推理速度显著下降。

## Evidence

[质询]该陈述包含具体的性能量化指标（'推理速度下降 30% 以上'）和特定的版本依赖关系（ROCm 6.1+ 对 Qwen3 FlashAttention-2 的支持），属于经验事实。在缺乏外部来源支持的情况下，无法验证该具体数值和版本阈值的准确性，且不同硬件配置和模型规模下性能差异可能显著，'30%'这一具体数值缺乏普遍性依据。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

ROCm 6.0 vLLM Qwen3 FlashAttention-2 support
