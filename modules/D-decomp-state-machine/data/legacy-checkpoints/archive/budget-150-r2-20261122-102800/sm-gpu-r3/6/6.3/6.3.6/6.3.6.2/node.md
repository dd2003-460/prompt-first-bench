# N361: RTX 4090 不支持原生 FP8 硬件加速，若强制使用 FP8 模型（如通过软件模拟或 CPU offload），其推理吞吐量将下降至 BF16 模式的 3

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N142

## Claim

RTX 4090 不支持原生 FP8 硬件加速，若强制使用 FP8 模型（如通过软件模拟或 CPU offload），其推理吞吐量将下降至 BF16 模式的 30-50% 以下，且延迟显著增加，因此 RTX 4090 在 FP8 口径下的性价比为负值或极低，应排除出 FP8 候选集。

## Corrected Claim

RTX 4090 不支持原生 FP8 硬件加速，若强制使用 FP8 模型，其推理吞吐量将显著低于 BF16 模式（具体降幅取决于软件实现，通常性能损失较大），因此 RTX 4090 在 FP8 口径下的性价比极低，应排除出 FP8 候选集。

## Evidence

[质询]具体数值区间（30-50%）缺乏通用基准测试支持，不同软件栈（如 TensorRT vs PyTorch）和模型架构下性能衰减比例差异巨大，该具体数值可能过于绝对或基于特定非最优配置。 | 先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada Lovelace) 确实缺乏原生 FP8 硬件加速单元（相比 Hopper 架构），强制使用 FP8 需依赖软件模拟或转换，必然导致性能显著下降，定性结论正确，但具体量化数值缺乏来源支持且存在变数。

## Search Query

RTX 4090 FP8 emulation performance penalty LLM
