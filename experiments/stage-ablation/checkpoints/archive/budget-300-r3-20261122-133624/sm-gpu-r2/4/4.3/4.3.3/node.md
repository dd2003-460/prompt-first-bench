# N104: RTX 5090 (Blackwell) 上 NVFP4 支持的驱动与框架依赖：需 NVIDIA 驱动版本 ≥ 555.55 及 CUDA 12.8+，且 vL

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

RTX 5090 (Blackwell) 上 NVFP4 支持的驱动与框架依赖：需 NVIDIA 驱动版本 ≥ 555.55 及 CUDA 12.8+，且 vLLM 需启用 --quantization nvfp4 参数；若驱动不达标，NVFP4 模型将报错或自动降级为 FP16，导致显存占用翻倍（从 ~14GB 增至 54GB），直接违反 32GB 显存约束。

## Corrected Claim

RTX 5090 (Blackwell) 上 NVFP4 支持需特定版本的 NVIDIA 驱动及 CUDA 12.8+，且 vLLM 需启用 --quantization nvfp4 参数；若驱动不达标，NVFP4 模型将报错或自动降级为 FP16，导致显存占用显著增加，可能违反显存约束。

## Evidence

[质询]具体驱动版本号（555.55）和显存占用数值（14GB/54GB）属于经验事实，缺乏来源支持，且不同模型大小下显存占用差异巨大，具体数值可能不准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 5090 NVFP4 vLLM driver version requirement
