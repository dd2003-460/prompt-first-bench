# N169: FP8/INT8 软件加速对 W4 基线吞吐的提升系数：在 MLX 框架下，FP8 推理相比 W4 通常提升 15-25% (因减少内存读取量)，但受限于 M2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

FP8/INT8 软件加速对 W4 基线吞吐的提升系数：在 MLX 框架下，FP8 推理相比 W4 通常提升 15-25% (因减少内存读取量)，但受限于 M2 Ultra 不支持原生 FP8 矩阵乘法 (需软件模拟)，实际提升可能低于理论值，需实测验证 ΔThroughput_FP8_W4

## Corrected Claim

在 MLX 框架下，FP8 推理相比 W4 基线通常因减少内存读取量而带来一定程度的吞吐提升，但具体提升幅度（如 15-25%）受限于 M2 Ultra 对 FP8 原生矩阵乘法的支持情况（若需软件模拟则提升受限），实际性能需通过实测验证。

## Evidence

[质询]该陈述包含具体的经验性能数据（15-25%提升）和特定硬件限制（M2 Ultra不支持原生FP8矩阵乘法），属于经验事实。由于检索无可用来源，无法验证这些具体数值和硬件特性的准确性，且不同模型架构和量化实现下性能差异巨大，单一数值区间可能具有误导性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

MLX framework M2 Ultra FP8 vs INT4 inference speedup Qwen 27B
