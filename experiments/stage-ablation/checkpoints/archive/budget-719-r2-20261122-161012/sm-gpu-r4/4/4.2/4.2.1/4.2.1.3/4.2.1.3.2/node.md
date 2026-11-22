# N501: 在 BF16 精度下，H100 SXM 的 32K 上下文 Prefill 延迟 T_prefill 约为 5.8 秒，基于 3.12 TFLOPs 计算量、9

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N206

## Claim

在 BF16 精度下，H100 SXM 的 32K 上下文 Prefill 延迟 T_prefill 约为 5.8 秒，基于 3.12 TFLOPs 计算量、990 TFLOPS 峰值算力及 55% MFU 估算，虽优于 RTX 4090 但仍高于 2.0s 严格阈值，需结合业务容忍度评估。

## Corrected Claim

在 BF16 精度下，H100 SXM 的 32K 上下文 Prefill 延迟 T_prefill 约为 5.8 秒，基于 3.12 TFLOPs 计算量、990 TFLOPS 峰值算力及 55% MFU 估算，虽优于 RTX 4090 但仍高于 2.0s 严格阈值，需结合业务容忍度评估。

## Evidence

先验知识/题面给定，逻辑校验通过：计算量3.12 TFLOPs / (990 TFLOPS * 55%) ≈ 5.74秒，与5.8秒一致；H100 SXM性能优于RTX 4090符合硬件常识。

## Search Query

H100 SXM Qwen3 27B 32K context prefill latency
