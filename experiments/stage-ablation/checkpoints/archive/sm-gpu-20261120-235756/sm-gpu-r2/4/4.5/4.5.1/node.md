# N95: Prefill 阶段（计算密集）TTFT 主导因素：FLOPs 需求 = 2 * N_params * Seq_Len，RTX 5090 (FP8 ~1000 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

Prefill 阶段（计算密集）TTFT 主导因素：FLOPs 需求 = 2 * N_params * Seq_Len，RTX 5090 (FP8 ~1000 TFLOPS) vs H100 (FP8 ~1979 TFLOPS)，理论 TTFT 比值约为 1.98x，即 H100 首字延迟约为 5090 的 50%。

## Corrected Claim

Prefill 阶段（计算密集）TTFT 主导因素：FLOPs 需求 = 2 * N_params * Seq_Len，RTX 5090 (FP8 ~1000 TFLOPS) vs H100 (FP8 ~1979 TFLOPS)，理论 TTFT 比值约为 1.98x，即 H100 首字延迟约为 5090 的 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：FLOPs公式正确，硬件规格（RTX 5090 ~1000 TFLOPS, H100 ~1979 TFLOPS）符合公开数据量级，比值计算（1979/1000 ≈ 1.98）及延迟反比关系逻辑自洽。

## Search Query

RTX 5090 vs H100 FP8 TFLOPS prefill latency
