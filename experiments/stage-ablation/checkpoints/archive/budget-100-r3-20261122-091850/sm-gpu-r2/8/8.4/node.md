# N114: ROCm 6.x 对 Qwen3-27B 的支持稳定性：在 vLLM 0.5+ 版本中，MI300X 运行 Qwen3 可能出现 NaN 值或 Kernel 编

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32, N33, N34

## Claim

ROCm 6.x 对 Qwen3-27B 的支持稳定性：在 vLLM 0.5+ 版本中，MI300X 运行 Qwen3 可能出现 NaN 值或 Kernel 编译失败，需使用特定的环境变量 (HSA_OVERRIDE_GFX_VERSION=10.3.0) 才能稳定运行，该兼容性风险导致运维复杂度增加，预估每年因软件 Bug 导致的停机时间比 CUDA 环境多 5-10 小时。

## Corrected Claim

ROCm 6.x 对 Qwen3-27B 的支持可能存在稳定性问题，在 vLLM 0.5+ 版本中，MI300X 运行 Qwen3 可能出现 NaN 值或 Kernel 编译失败，可能需要特定的环境变量配置才能稳定运行，该兼容性风险可能导致运维复杂度增加。

## Evidence

[质询]该陈述包含具体的经验性数值（每年多5-10小时停机时间）和特定的技术配置（HSA_OVERRIDE_GFX_VERSION=10.3.0），属于经验事实而非第一性原理可推导内容。在缺乏任何外部来源支持的情况下，无法验证这些具体数值和配置参数的准确性及普遍性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

ROCm MI300X Qwen3 vLLM compatibility issues NaN error
