# N499: H100 SXM 在 Qwen3-27B BF16 Prefill 阶段的实测 MFU 约为 55%，得益于 Hopper 架构的 FP8/TF32 支持优化及

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N205

## Claim

H100 SXM 在 Qwen3-27B BF16 Prefill 阶段的实测 MFU 约为 55%，得益于 Hopper 架构的 FP8/TF32 支持优化及 HBM3 高带宽对 Attention 算子计算的支撑。

## Corrected Claim

H100 SXM 在 Qwen3-27B BF16 Prefill 阶段的实测 MFU 可达较高水平（如 50% 以上），主要得益于 Hopper 架构的高算力 Tensor Core 及 HBM3 高带宽对 Attention 算子计算的支撑。

## Evidence

[质询]55% MFU 是一个具体的经验性能指标，受具体序列长度、Batch Size、Kernel 实现及硬件微调影响极大，并非固定常数；且 BF16 计算主要依赖 Tensor Core 的 BF16 路径，而非 FP8/TF32（除非特定混合精度策略），归因于 FP8/TF32 支持可能存在技术细节上的不精确或混淆。 | source=knowledge，逻辑上 H100 高带宽和架构优化确实能支撑高 MFU，55% 在合理量级范围内，但具体数值及归因细节缺乏直接来源支持，且存在技术归因模糊性，故降级。

## Search Query

H100 SXM Qwen3 27B prefill MFU benchmark
