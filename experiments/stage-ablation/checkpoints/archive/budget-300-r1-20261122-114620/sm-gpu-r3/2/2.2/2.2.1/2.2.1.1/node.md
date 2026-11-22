# N189: A100 80GB 在 Qwen3-27B BF16, batch=1, 32K 上下文下的 Prefill 阶段延迟 T_prefill 约为 3.2-4.5

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

A100 80GB 在 Qwen3-27B BF16, batch=1, 32K 上下文下的 Prefill 阶段延迟 T_prefill 约为 3.2-4.5 秒，计算公式为 T_prefill ≈ (2 * P_params * L_ctx) / (Peak_FLOPS * MFU)，其中 P_params=27e9, L_ctx=32768, Peak_FLOPS=312 TFLOPS, MFU(Machine Utilization) 在长上下文下通常降至 40-50% [待核验]。

## Corrected Claim

A100 80GB 在 Qwen3-27B BF16, batch=1, 32K 上下文下的 Prefill 阶段延迟 T_prefill 估算约为 3.2-4.5 秒（基于 MFU 40-50% 的假设），实际延迟取决于具体推理引擎优化程度。

## Evidence

[质询]该陈述包含具体的经验性能数值（3.2-4.5秒）和硬件利用率假设（MFU 40-50%），属于经验事实而非第一性原理可严格推导的数学/物理定律。虽然公式逻辑自洽，但缺乏外部来源直接支持具体延迟数值和MFU取值范围，且不同实现（如FlashAttention版本、算子优化程度）可能导致显著差异。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

NVIDIA A100 80GB LLM inference prefill latency 32k context Qwen 27B benchmark
