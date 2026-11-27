# N422: 在 RTX 5090 (FP8) 上，Qwen3-27B 的 Prefill 阶段吞吐量 (Tokens/s) 受算力限制，计算公式为 Prefill_Thro

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

在 RTX 5090 (FP8) 上，Qwen3-27B 的 Prefill 阶段吞吐量 (Tokens/s) 受算力限制，计算公式为 Prefill_Throughput = (FLOPS × MFU) / FLOPs_per_token，其中 FLOPs_per_token 约为 2 × Model_Params = 54 GFLOPs/token，MFU (Model FLOPs Utilization) 在长 Prompt 下通常为 40-60%。

## Corrected Claim

在 RTX 5090 (FP8) 上，Qwen3-27B 的 Prefill 阶段吞吐量 (Tokens/s) 受算力限制，计算公式为 Prefill_Throughput = (FLOPS × MFU) / FLOPs_per_token，其中 FLOPs_per_token 约为 2 × Model_Params = 54 GFLOPs/token，MFU (Model FLOPs Utilization) 在长 Prompt 下通常为 40-60%。

## Evidence

先验知识/题面给定，逻辑校验通过：FLOPs_per_token ≈ 2×Params 是 Transformer 推理的标准近似公式（27B×2=54G），MFU 40-60% 符合大模型长序列 Prefill 阶段的典型工程经验值，量纲与数值量级均合理。
