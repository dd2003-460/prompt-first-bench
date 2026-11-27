# N99: Qwen3-27B 在 32K 上下文下的 Prefill 阶段计算量（FLOPs）约为 2 * 27e9 * 32768 ≈ 1.77 TFLOPs，Pref

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

Qwen3-27B 在 32K 上下文下的 Prefill 阶段计算量（FLOPs）约为 2 * 27e9 * 32768 ≈ 1.77 TFLOPs，Prefill 延迟 T_prefill = 1.77e12 / (GPU_FLOPS * MFU)，其中 MFU (Model FLOPs Utilization) 在主流推理引擎中通常为 30%-50%。

## Corrected Claim

Qwen3-27B 在 32K 上下文下的 Prefill 阶段计算量（FLOPs）约为 2 * 27e9 * 32768 ≈ 1.77 TFLOPs，Prefill 延迟 T_prefill = 1.77e12 / (GPU_FLOPS * MFU)，其中 MFU (Model FLOPs Utilization) 在主流推理引擎中通常为 30%-50%。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 207 (char 273)

## Search Query

Qwen3-27B prefill FLOPs calculation 32k context
