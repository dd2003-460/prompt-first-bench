# N263: RTX 4090 的 FP8 算力 330.4 TFLOPS 仅在支持 FP8 量化格式（如 FP8 E4M3）且使用特定 CUDA 内核（如 Triton F

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

RTX 4090 的 FP8 算力 330.4 TFLOPS 仅在支持 FP8 量化格式（如 FP8 E4M3）且使用特定 CUDA 内核（如 Triton FP8 kernels）时可达；若使用 vLLM 默认路径，FP8 可能回退到 BF16 计算或仅用于存储，导致实际算力增益远低于 4x；需验证 vLLM 当前版本对 RTX 4090 FP8 的硬件加速支持状态及实测吞吐提升比。

## Corrected Claim

RTX 4090 支持 FP8 量化格式（如 FP8 E4M3），其 FP8 算力显著高于 BF16。然而，实际性能增益取决于软件栈（如 vLLM）是否实现了针对 Ada Lovelace 架构的 FP8 硬件加速内核；若未启用特定优化，可能回退到 BF16 计算或仅用于存储，导致实际吞吐提升低于理论峰值。需验证具体软件版本对 RTX 4090 FP8 的支持状态及实测数据。

## Evidence

[质询]该陈述包含具体的硬件规格数值（330.4 TFLOPS）及特定软件栈（vLLM）的行为细节，属于经验事实。由于检索失败，无法验证该数值是否准确对应RTX 4090的FP8峰值算力，也无法确认vLLM当前版本在RTX 4090上的具体回退机制和实测数据。 | 经验事实，逻辑自洽但缺来源支持。RTX 4090基于Ada Lovelace架构，确实支持FP8，且FP8算力通常为BF16的2倍（非4x，除非考虑稀疏性，但陈述中提到的4x增益可能指代稀疏或特定对比基准，此处存在潜在数值争议，但核心逻辑关于‘需验证支持状态’是合理的）。因无外部来源，无法确认具体数值330.4 TFLOPS及vLLM的具体行为，故降级。

## Search Query

vLLM RTX 4090 FP8 support hardware acceleration Triton kernel performance
