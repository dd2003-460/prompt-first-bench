# N771: 在 vLLM 或 TensorRT-LLM 中，Decode 阶段 Batch Size=1 时，每个 Transformer 层的 LayerNorm、Sof

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N239

## Claim

在 vLLM 或 TensorRT-LLM 中，Decode 阶段 Batch Size=1 时，每个 Transformer 层的 LayerNorm、Softmax 及 Residual Add 等非 GEMM 操作的总耗时约为 0.5-1.0ms，占单层总耗时的 15-30%，导致实际带宽利用率下降。

## Corrected Claim

在 vLLM 或 TensorRT-LLM 中，Decode 阶段 Batch Size=1 时，LayerNorm、Softmax 及 Residual Add 等非 GEMM 操作的耗时占比显著高于 Prefill 阶段，通常占单层总耗时的 15-30% 甚至更高，导致实际带宽利用率下降。

## Evidence

[质询]该陈述包含具体的经验性数值（0.5-1.0ms, 15-30%），这些数值高度依赖于硬件架构（如A100/H100）、模型规模（如7B/70B）及具体实现优化程度，并非普适常数。在缺乏特定硬件和模型上下文的情况下，直接断言固定数值范围属于过度概括，且检索无来源支持该具体量级。 | 经验事实，逻辑自洽（非GEMM操作确实存在且占比随Batch Size减小而上升），但缺来源支持具体数值范围，且数值具有硬件/模型依赖性。

## Search Query

vLLM decode phase non-GEMM overhead latency profile LayerNorm Softmax ms
