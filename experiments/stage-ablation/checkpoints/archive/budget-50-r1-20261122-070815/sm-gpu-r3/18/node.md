# N449: Intel Gaudi 3 或 AMD MI250 等数据中心级非 NVIDIA 加速器在 LLM 推理中的软件栈成熟度评分低于 6/10（基于社区反馈），主要

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Intel Gaudi 3 或 AMD MI250 等数据中心级非 NVIDIA 加速器在 LLM 推理中的软件栈成熟度评分低于 6/10（基于社区反馈），主要瓶颈在于 vLLM/TensorRT-LLM 的原生支持缺失及算子优化不足，导致实际吞吐量仅为理论值的 40-60%，因此在‘本地工作站’且‘无硬性延迟指标’的前提下，若排除 NVIDIA 生态，这些方案因部署复杂度（Setup Cost）过高而不具备性价比优势，除非其硬件价格低于 $5,000

## Corrected Claim

Intel Gaudi 3 或 AMD MI250 等数据中心级非 NVIDIA 加速器在 LLM 推理中的软件栈成熟度评分低于 6/10（基于社区反馈），主要瓶颈在于 vLLM/TensorRT-LLM 的原生支持缺失及算子优化不足，导致实际吞吐量仅为理论值的 40-60%，因此在‘本地工作站’且‘无硬性延迟指标’的前提下，若排除 NVIDIA 生态，这些方案因部署复杂度（Setup Cost）过高而不具备性价比优势，除非其硬件价格低于 $5,000

## Evidence

检索失败: no sources from any channel (all 5 failed)
