# N246: A100 SXM4 在 vLLM 推理 Qwen3-27B (BF16/FP8) 时的 GPU 利用率 (Utilization) 分布：Prefill 阶段接

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

A100 SXM4 在 vLLM 推理 Qwen3-27B (BF16/FP8) 时的 GPU 利用率 (Utilization) 分布：Prefill 阶段接近 100%，Decode 阶段通常降至 60-80%，整体加权平均利用率需根据请求并发数 (Concurrency) 和上下文长度分布 (Context Length Distribution) 计算，无法用单一固定值 50-70% 概括。

## Corrected Claim

A100 SXM4 在 vLLM 推理 Qwen3-27B (BF16/FP8) 时的 GPU 利用率 (Utilization) 分布：Prefill 阶段接近 100%，Decode 阶段通常降至 60-80%，整体加权平均利用率需根据请求并发数 (Concurrency) 和上下文长度分布 (Context Length Distribution) 计算，无法用单一固定值 50-70% 概括。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill为计算密集型（Compute-bound），GPU利用率通常接近100%；Decode为访存密集型（Memory-bound），受限于显存带宽，利用率通常低于Prefill（60-80%符合常见经验值）；整体利用率确实随并发和上下文长度动态变化，无法用单一固定值概括。

## Search Query

vLLM A100 GPU utilization prefill decode ratio inference benchmark
