# N165: 不同硬件对 FP8 KV Cache 的支持性验证：RTX 4090 (Ada Lovelace) 和 A100 (Ampere) 均原生支持 FP8 数据格式

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

不同硬件对 FP8 KV Cache 的支持性验证：RTX 4090 (Ada Lovelace) 和 A100 (Ampere) 均原生支持 FP8 数据格式，但需确认推理框架 (如 vLLM, TensorRT-LLM) 是否已实现 FP8 KV Cache 的优化内核，否则需软件模拟导致性能损失。

## Corrected Claim

不同硬件对 FP8 KV Cache 的支持性验证：H100 (Hopper) 原生支持 FP8 数据格式，而 RTX 4090 (Ada Lovelace) 和 A100 (Ampere) 不原生支持 FP8，需通过软件模拟或量化转换（如转换为 INT8/FP16）来实现，否则无法利用硬件加速。

## Evidence

[质询]事实错误：RTX 4090 (Ada Lovelace) 和 A100 (Ampere) 均不原生支持 FP8 数据格式。FP8 支持是 Hopper 架构 (H100) 及后续架构 (如 Ada Lovelace 的某些特定指令集或 Blackwell) 的特性，Ampere 和 Ada Lovelace 的 Tensor Core 原生支持 FP16/BF16/INT8，但不支持 FP8 硬件加速。 | 无可用外部证据。基于硬件架构常识，Ampere (A100) 和 Ada Lovelace (RTX 4090) 均不支持原生 FP8 计算，该陈述存在硬事实错误。

## Search Query

vLLM TensorRT-LLM FP8 KV cache support RTX 4090 A100 performance overhead
