# N110: 条件分支1（预算<$3,000, W4量化）的硬件可行性验证：2× RTX 3090 (48GB总显存) 在 W4 量化下总显存需求为 35.18GB (N8)

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

条件分支1（预算<$3,000, W4量化）的硬件可行性验证：2× RTX 3090 (48GB总显存) 在 W4 量化下总显存需求为 35.18GB (N8)，剩余 12.82GB 用于 KV Cache 扩展及激活值，需确认 KV Cache 是否支持 FP8 量化以进一步降低占用（N10），若不支持则需验证 48GB 是否足以支持 32K 上下文及 Batch Size=1 的完整推理流程。

## Corrected Claim

2× RTX 3090 (48GB总显存) 在 W4 量化下模型权重占用约 35.18GB，剩余显存用于 KV Cache 及激活值。需进一步验证在 32K 上下文及 Batch Size=1 条件下，剩余显存是否足以支撑完整推理流程，特别是需确认 KV Cache 量化支持情况以优化显存占用。

## Evidence

[质询]该陈述包含具体的硬件参数（RTX 3090 显存、W4量化后模型大小35.18GB）和推理资源需求（KV Cache、激活值），属于经验事实。由于检索失败，无法验证35.18GB这一具体数值是否准确对应特定模型在W4量化下的真实占用，也无法确认48GB显存是否确实足以支持32K上下文及Batch Size=1的完整推理（特别是考虑到激活值在长上下文下的显存开销可能远超剩余空间）。 | 经验事实，逻辑自洽但缺来源支持。虽然48GB > 35.18GB在算术上成立，但剩余12.82GB是否足以覆盖32K上下文的KV Cache和激活值属于经验性判断，且无外部来源佐证具体数值和可行性结论。

## Search Query

RTX 3090 W4 quantization Qwen3-27B 32K context KV cache memory usage vLLM
