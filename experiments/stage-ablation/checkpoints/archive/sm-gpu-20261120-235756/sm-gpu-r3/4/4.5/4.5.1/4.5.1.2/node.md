# N270: H100 (SXM) 在 FP8 精度下，Qwen3-27B 32K 上下文 Prefill 阶段的理论 FLOPs 需求同上 (1.78 PFLOPs)，基于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

H100 (SXM) 在 FP8 精度下，Qwen3-27B 32K 上下文 Prefill 阶段的理论 FLOPs 需求同上 (1.78 PFLOPs)，基于 H100 FP8 峰值算力 ~1979 TFLOPS (1.979 PFLOPS)，理论最小 Prefill 时间 = 0.90s，考虑 50-60% 利用率，实际 TTFT 约 1.50-1.80s

## Corrected Claim

H100 (SXM) 在 FP8 精度下，Qwen3-27B 32K 上下文 Prefill 阶段的理论 FLOPs 需求同上 (1.78 PFLOPs)，基于 H100 FP8 峰值算力 ~1979 TFLOPS (1.979 PFLOPS)，理论最小 Prefill 时间 = 0.90s，考虑 50-60% 利用率，实际 TTFT 约 1.50-1.80s

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM FP8 峰值算力约 1979 TFLOPS 符合硬件规格，1.78 PFLOPs / 1.979 PFLOPS ≈ 0.90s 计算正确，50-60% 利用率推导出的 1.50-1.80s 时间范围逻辑自洽。
