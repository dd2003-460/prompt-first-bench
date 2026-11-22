# N663: AMD RX 7900 XTX 在 Qwen3-27B INT4 量化下的 ROCm 兼容性状态：截至 2024 Q4，ROCm 6.0 对 Qwen3-27B

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N236

## Claim

AMD RX 7900 XTX 在 Qwen3-27B INT4 量化下的 ROCm 兼容性状态：截至 2024 Q4，ROCm 6.0 对 Qwen3-27B 的 vLLM/TensorRT-LLM 支持尚处于实验阶段，缺乏官方优化的量化内核（如 AWQ/GPTQ），导致 Prefill 阶段计算性能较 CUDA 版本低 30-50% [search: 'ROCm 6.0 Qwen3-27B vLLM compatibility status 2024']

## Corrected Claim

AMD RX 7900 XTX 在 Qwen3-27B INT4 量化下的 ROCm 兼容性状态：截至 2024 Q4，ROCm 对 Qwen3-27B 的 vLLM/TensorRT-LLM 支持可能尚处于实验阶段，缺乏官方优化的量化内核（如 AWQ/GPTQ），导致 Prefill 阶段计算性能较 CUDA 版本存在显著差距。

## Evidence

[质询]该陈述包含具体的性能损耗数值（30-50%）和特定的软件版本支持状态（ROCm 6.0 对 Qwen3-27B 的实验阶段支持），属于经验事实。由于检索失败，无法验证这些具体数值和状态是否准确，且不同硬件配置和软件版本下性能差异可能波动较大，存在数值量级不准确的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

ROCm 6.0 Qwen3-27B vLLM compatibility status 2024
