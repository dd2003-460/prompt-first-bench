# N53: FP8 量化实现依赖项：FP8 推理需要硬件原生支持（如 Ada Lovelace 4090 支持 FP8 tensor cores, Ampere 3090 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

FP8 量化实现依赖项：FP8 推理需要硬件原生支持（如 Ada Lovelace 4090 支持 FP8 tensor cores, Ampere 3090 不支持需软件模拟）。4090 上 FP8 权重+BF16 计算 (W8A16) 与 FP8 权重+FP8 计算 (W8A8) 的延迟差异约 10-20%，影响 TPS。

## Corrected Claim

FP8 量化实现依赖项：FP8 推理需要硬件原生支持（如 Ada Lovelace 4090 支持 FP8 tensor cores, Ampere 3090 不支持需软件模拟）。4090 上 FP8 权重+BF16 计算 (W8A16) 与 FP8 权重+FP8 计算 (W8A8) 的延迟差异约 10-20%，影响 TPS。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了硬件能力（4090原生支持）、性能差异机制（W8A16 vs W8A8）以及硬件限制（3090不支持），三者维度不同（硬件规格、算法/模式对比、兼容性/模拟开销），无重复或矛盾，且完整覆盖了父节点关于硬件依赖、两种模式延迟差异及3090限制的所有关键点。）

## Search Query

RTX 4090 FP8 inference performance vs BF16
