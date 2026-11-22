# N356: Apple M3 Ultra 在 FP8/INT8 精度下运行 Qwen3-27B 的吞吐量损失倍数需通过实测基准确定：BF16 理论 TPOT 为 2.72m

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N135

## Claim

Apple M3 Ultra 在 FP8/INT8 精度下运行 Qwen3-27B 的吞吐量损失倍数需通过实测基准确定：BF16 理论 TPOT 为 2.72ms/token (54.36GB / 800GB/s)，FP8 理论 TPOT 为 1.36ms/token (27.18GB / 800GB/s)，理论加速比为 2.0x；但 M3 Ultra 缺乏原生 FP8 Tensor Core 支持，实际 FP8 推理需依赖 CPU/ANE 混合加速或软件模拟，导致实际加速比可能降至 1.2x-1.5x [待核验]，需检索 M3 Ultra FP8 推理实测数据。

## Corrected Claim

Apple M3 Ultra 在 FP8/INT8 精度下运行 Qwen3-27B 的吞吐量损失倍数需通过实测基准确定：BF16 理论 TPOT 为 2.72ms/token (54.36GB / 800GB/s)，FP8 理论 TPOT 为 1.36ms/token (27.18GB / 800GB/s)，理论加速比为 2.0x；由于 M3 Ultra 可能缺乏原生 FP8 硬件加速支持，实际加速比可能低于理论值，具体数值需检索 M3 Ultra FP8 推理实测数据。

## Evidence

[质询]该陈述包含具体的硬件性能参数（M3 Ultra 内存带宽 800GB/s）和实测推断（实际加速比 1.2x-1.5x），属于经验事实。虽然 BF16 到 FP8 的理论加速比 2.0x 符合数学逻辑，但 M3 Ultra 缺乏原生 FP8 Tensor Core 支持以及具体的实际加速比范围属于硬件规格和实测数据，无法仅从第一性原理严格推出，且当前无可用外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Apple M3 Ultra FP8 inference benchmark Qwen3-27B tokens per second
