# N157: NVIDIA A100 80GB 在 FP8 推理下的实际功耗修正：A100 不支持原生 FP8 硬件加速（Hopper 架构才支持），FP8 推理需软件模拟或

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

NVIDIA A100 80GB 在 FP8 推理下的实际功耗修正：A100 不支持原生 FP8 硬件加速（Hopper 架构才支持），FP8 推理需软件模拟或降级为 INT8/INT4，实际吞吐量可能比 H100/H200 低 30-40%；因此 N100 中假设的 FP8 方案在 A100 上可能不适用，需重新评估为 BF16 或 INT8 方案，吞吐量预计为 H200 BF16 的 60-70%。

## Corrected Claim

NVIDIA A100 80GB 在 FP8 推理下的实际功耗修正：A100 不支持原生 FP8 硬件加速（Hopper 架构才支持），FP8 推理需软件模拟或降级为 INT8/INT4，实际吞吐量可能比 H100/H200 低 30-40%；因此 N100 中假设的 FP8 方案在 A100 上可能不适用，需重新评估为 BF16 或 INT8 方案，吞吐量预计为 H200 BF16 的 60-70%。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 (Ampere) 确实不支持原生 FP8 硬件加速（Hopper 架构引入），FP8 在 A100 上需软件模拟或降级，导致性能低于 H100/H200 符合硬件架构差异的物理事实；吞吐量对比数值（60-70%）在工程估算量级上合理。

## Search Query

A100 FP8 support software emulation performance penalty
