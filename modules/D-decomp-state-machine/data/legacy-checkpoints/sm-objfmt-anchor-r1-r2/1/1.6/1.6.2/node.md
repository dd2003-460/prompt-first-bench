# N51: 老旧数据中心卡 (P40/V100) 的驱动支持现状：CUDA 12.4 为最后支持的版本，NVIDIA 已停止为其提供新特性更新；vLLM 0.6+ 版本要求

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

老旧数据中心卡 (P40/V100) 的驱动支持现状：CUDA 12.4 为最后支持的版本，NVIDIA 已停止为其提供新特性更新；vLLM 0.6+ 版本要求 CUDA >= 12.0，但部分优化 kernel (如 FlashAttention-3) 仅支持 Ampere+ 架构，导致 P40/V100 无法使用最新加速特性，吞吐量较新卡低 30-50% [待核验]。

## Corrected Claim

老旧数据中心卡 (P40/V100) 的驱动支持现状：CUDA 12.4 为最后支持的版本，NVIDIA 已停止为其提供新特性更新；vLLM 等现代推理框架要求较高的 CUDA 版本，且部分优化 kernel (如 FlashAttention-3) 仅支持 Ampere+ 架构，导致 P40/V100 无法使用最新加速特性，吞吐量通常显著低于新卡。

## Evidence

[质询]具体数值（吞吐量低30-50%）和特定软件版本依赖（vLLM 0.6+）属于经验事实，缺乏来源支持，且不同工作负载下性能差异巨大，固定百分比可能不准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVIDIA P40 V100 CUDA 12.4 driver support vLLM FlashAttention-3 architecture compatibility
