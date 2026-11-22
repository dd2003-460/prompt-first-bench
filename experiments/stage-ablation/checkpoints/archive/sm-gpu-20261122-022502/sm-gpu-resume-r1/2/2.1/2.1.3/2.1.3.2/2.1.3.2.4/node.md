# N558: RX 9070 XT FP8 推理实际加速比：假设 ROCm 优化后，RX 9070 XT FP8 推理吞吐约为 FP16 的 1.5 倍，即 960 GB/s

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N171

## Claim

RX 9070 XT FP8 推理实际加速比：假设 ROCm 优化后，RX 9070 XT FP8 推理吞吐约为 FP16 的 1.5 倍，即 960 GB/s * 1.5 / 13.5GB ≈ 106.7 tokens/s [待核验：实际测量值]

## Corrected Claim

RX 9070 XT FP8 推理吞吐取决于实际带宽和模型大小，若假设带宽为 960 GB/s 且 FP8 相比 FP16 有 1.5 倍加速，理论吞吐约为 106.7 tokens/s，但实际值需以测量为准。

## Evidence

[质询]该陈述包含具体的硬件性能参数（960 GB/s 带宽、13.5GB 模型大小）和未经证实的优化假设（ROCm 优化后 FP8 加速比 1.5 倍），属于经验事实，且缺乏实际测量数据支持，加速比和带宽数值可能因具体驱动版本、模型架构及内存配置而异。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值和加速比假设）

## Search Query

RX 9070 XT FP8 inference tokens per second benchmark llama.cpp
