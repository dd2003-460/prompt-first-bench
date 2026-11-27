# N314: 工作点 B (中 MFU ~40%)：使用 vLLM 默认配置 (CUDA Graphs 未完全优化或 Batch Size 较小) 时，RTX 4090 在 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N111

## Claim

工作点 B (中 MFU ~40%)：使用 vLLM 默认配置 (CUDA Graphs 未完全优化或 Batch Size 较小) 时，RTX 4090 在 BF16 预填充阶段的 MFU 通常在 35-45%，主要瓶颈为内核启动开销和内存带宽竞争

## Corrected Claim

工作点 B (中 MFU)：使用 vLLM 默认配置时，RTX 4090 在 BF16 预填充阶段的 MFU 通常处于中等水平（具体数值需实测，一般低于峰值），主要瓶颈为内核启动开销和内存带宽竞争。

## Evidence

[质询]该陈述包含具体的经验性数值范围（35-45%）和特定硬件/软件配置下的性能表现，属于经验事实。由于检索无可用来源，无法验证该具体数值区间的准确性，且不同vLLM版本、CUDA版本及具体模型架构可能导致MFU波动较大，存在数值量级或具体区间不准确的风险。 | 经验事实，逻辑自洽（RTX 4090在BF16预填充阶段受内存带宽和内核启动开销限制，MFU低于峰值是合理的），但缺来源支持。

## Search Query

vLLM RTX 4090 prefill MFU efficiency benchmark
