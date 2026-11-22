# N115: NVIDIA L4 运行 Qwen3-27B INT8/FP8 在 32K 上下文下的实测吞吐量基准：由于 L4 无 FP8 Tensor Core 原生支持（

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

NVIDIA L4 运行 Qwen3-27B INT8/FP8 在 32K 上下文下的实测吞吐量基准：由于 L4 无 FP8 Tensor Core 原生支持（Ada Lovelace 架构主要优化 FP32/TF32/INT8），FP8 可能回退到 FP16 模拟或 INT8 转换，需量化此回退导致的额外计算开销对 tokens/s 的影响。

## Corrected Claim

NVIDIA L4 (Ada Lovelace 架构) 不支持原生 FP8 Tensor Core 加速，运行 Qwen3-27B FP8 模型时需回退至 FP16 或 INT8 路径，这将导致相比原生 FP8 硬件（如 H100）更高的计算开销和更低的吞吐量，具体 tokens/s 数值需依赖特定推理框架（如 TensorRT-LLM）的实测基准。

## Evidence

[质询]该陈述包含具体的硬件架构特性（L4无FP8原生支持）和性能基准（32K上下文吞吐量），属于经验事实。虽然架构特性符合已知事实，但具体的吞吐量数值及回退开销的具体量化数据缺乏来源支持，且不同量化实现（如TensorRT-LLM vs vLLM）可能导致结果差异巨大，无法仅凭逻辑推导得出精确基准。 | 经验事实，逻辑自洽但缺来源支持。NVIDIA L4 (Ada Lovelace) 确实不支持原生 FP8 Tensor Core 加速（FP8 支持始于 Hopper H100），因此 FP8 模型在 L4 上运行必然涉及精度转换或模拟，导致性能低于原生 FP8 硬件。但具体的 tokens/s 基准值属于实测数据，无来源覆盖，故降级。

## Search Query

NVIDIA L4 Qwen3-27B INT8 FP8 inference speed tokens/s 32k context
