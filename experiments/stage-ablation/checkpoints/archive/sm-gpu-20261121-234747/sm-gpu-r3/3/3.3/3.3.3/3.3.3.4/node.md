# N263: L40S在FP8精度下Prefill阶段（处理32K上下文）的吞吐量（tokens/s）受限于计算瓶颈（Compute-Bound），估算公式：Prefill_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94, N95, N96

## Claim

L40S在FP8精度下Prefill阶段（处理32K上下文）的吞吐量（tokens/s）受限于计算瓶颈（Compute-Bound），估算公式：Prefill_Throughput ≈ (Peak_FLOPS * Utilization) / (2 * Params * Seq_Len / Seq_Len) 简化为 Peak_FLOPS * Utilization / (2 * Params)，若利用率60%，则 Prefill ≈ 121,000 * 0.6 / (2 * 27) ≈ 1344 tokens/s，用于评估首字延迟（TTFT）

## Corrected Claim

L40S在FP8精度下Prefill阶段（处理32K上下文）的吞吐量（tokens/s）受限于计算瓶颈（Compute-Bound），估算公式：Prefill_Throughput ≈ (Peak_FLOPS * Utilization) / (2 * Params * Seq_Len / Seq_Len) 简化为 Peak_FLOPS * Utilization / (2 * Params)，若利用率60%，则 Prefill ≈ 121,000 * 0.6 / (2 * 27) ≈ 1344 tokens/s，用于评估首字延迟（TTFT）

## Evidence

先验知识/题面给定，逻辑校验通过：L40S FP8峰值算力约121 TFLOPS，27B参数模型Prefill阶段计算量约为2*Params*Tokens，公式推导及数值计算（121000*0.6/54 ≈ 1344）均符合逻辑与工程常识。

## Search Query

NVIDIA L40S prefill throughput 32k context benchmark
