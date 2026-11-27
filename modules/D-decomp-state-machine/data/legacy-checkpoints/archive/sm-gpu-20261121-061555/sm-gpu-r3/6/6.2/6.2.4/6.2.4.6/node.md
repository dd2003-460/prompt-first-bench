# N326: ROCm 对 Qwen3-27B 混合注意力架构（Gated DeltaNet）的支持状态：确认 ROCm 是否提供针对线性注意力层的高效 Kernel，若仅支

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114, N115, N117

## Claim

ROCm 对 Qwen3-27B 混合注意力架构（Gated DeltaNet）的支持状态：确认 ROCm 是否提供针对线性注意力层的高效 Kernel，若仅支持标准 MHA，评估将 Gated DeltaNet 层近似为 MHA 或 CPU Offload 带来的延迟增加（如 32K 上下文下每 Token 生成时间增加毫秒数）及显存占用变化。

## Corrected Claim

ROCm 对 Qwen3-27B 混合注意力架构（Gated DeltaNet）的支持状态需进一步确认：若 ROCm 未提供针对线性注意力层的高效 Kernel，仅支持标准 MHA，则需评估将 Gated DeltaNet 层近似为 MHA 或 CPU Offload 带来的延迟增加及显存占用变化（具体数值需实测验证）。

## Evidence

[质询]该陈述包含具体的性能量化指标（如32K上下文下每Token生成时间增加的毫秒数、显存占用变化），属于经验事实。当前无可用来源支持这些具体数值，且ROCm对Qwen3-27B混合架构（Gated DeltaNet）的具体Kernel支持状态及性能开销需实测数据支撑，无法仅凭逻辑推导得出具体毫秒数。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

ROCm Qwen3 Gated DeltaNet linear attention kernel support performance
