# N235: A100 硬件对 FP8 的支持机制验证：A100 (Ampere架构) 硬件原生仅支持 BF16/TF32/INT8 Tensor Core 运算，不支持 F

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

A100 硬件对 FP8 的支持机制验证：A100 (Ampere架构) 硬件原生仅支持 BF16/TF32/INT8 Tensor Core 运算，不支持 FP8 指令集；所谓 'A100 FP8 推理' 实为软件模拟或错误表述，若使用 TensorRT-LLM 的 FP8 功能，A100 会回退至 BF16 或 INT8 执行，导致 'FP8 加速' 在 A100 上不存在，吞吐量应与 BF16 持平或略低（因转换开销），此前提需修正为 'A100 不支持原生 FP8'。

## Corrected Claim

A100 (Ampere架构) 硬件原生不支持 FP8 Tensor Core 运算（FP8 支持始于 Hopper 架构）。在 A100 上声称的 'FP8 推理' 通常指软件层面的模拟或量化转换，而非原生硬件加速。使用支持 FP8 的框架（如 TensorRT-LLM）时，A100 会回退至 BF16 或 INT8 执行，因此不存在原生 FP8 硬件加速，实际吞吐量受软件转换开销影响，通常不会优于 BF16/INT8 原生执行。

## Evidence

[质询]该陈述包含具体的硬件规格（A100不支持FP8）和软件行为（TensorRT-LLM回退机制），属于经验事实。虽然逻辑上Ampere架构确实早于FP8支持（Hopper架构引入），但缺乏直接来源证实TensorRT-LLM在A100上的具体回退行为及吞吐量表现（持平或略低），且‘吞吐量应与BF16持平或略低’这一性能预测缺乏实证数据支持，可能存在因模拟开销导致显著下降的情况。 | 经验事实，逻辑自洽（Ampere架构确实无原生FP8 Tensor Core，FP8由Hopper引入）但缺来源支持，且性能影响的具体量化描述（持平或略低）缺乏实证依据。

## Search Query

A100 Ampere architecture FP8 support Tensor Core instructions
