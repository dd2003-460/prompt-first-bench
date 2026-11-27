# N286: RTX 4090 对 FP8 精度的支持状态：硬件层面不支持原生 FP8 Tensor Core 计算（仅支持 BF16/FP16/INT8），软件层面需通过 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

RTX 4090 对 FP8 精度的支持状态：硬件层面不支持原生 FP8 Tensor Core 计算（仅支持 BF16/FP16/INT8），软件层面需通过 emulated FP8 (如 cutlass 或 vLLM 的 fp8 模拟) 实现，性能损失约为原生 FP8 的 1.5-2 倍，需引用 vLLM 或 TensorRT 文档验证

## Corrected Claim

RTX 4090 硬件层面不支持原生 FP8 Tensor Core 计算（仅支持 BF16/FP16/INT8 等），软件层面需通过 emulated FP8（如 cutlass 或 vLLM 的 fp8 模拟）实现，性能通常低于原生 FP8 硬件（具体损失倍数取决于实现方式，通常显著高于原生 FP8 但优于纯 FP16 模拟，需具体基准测试验证）。

## Evidence

[质询]该陈述包含具体的硬件规格（RTX 4090 不支持原生 FP8）和性能量化数据（1.5-2 倍损失），属于经验事实。由于本轮检索无可用来源，无法验证具体的性能损失倍数是否准确，且不同模拟实现（如 CUTLASS vs vLLM 特定 kernel）的性能差异可能较大，单一数值范围可能缺乏普适性。 | 经验事实，逻辑自洽（RTX 4090 确为 Ada Lovelace 架构，无原生 FP8 Tensor Core，需软件模拟），但缺来源支持具体性能损失数值。

## Search Query

RTX 4090 FP8 support vLLM TensorRT emulated fp8 performance overhead
