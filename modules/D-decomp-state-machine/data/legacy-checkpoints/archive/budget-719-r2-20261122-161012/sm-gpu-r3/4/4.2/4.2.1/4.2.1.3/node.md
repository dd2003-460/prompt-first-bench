# N206: 基于修正后的 FLOPs (3.12 TFLOPs) 和 MFU，RTX 4090 的 Prefill 延迟 T_prefill ≈ 3.12e12 / (33

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N99

## Claim

基于修正后的 FLOPs (3.12 TFLOPs) 和 MFU，RTX 4090 的 Prefill 延迟 T_prefill ≈ 3.12e12 / (330e9 * 0.45) ≈ 21 秒；H100 SXM 的 T_prefill ≈ 3.12e12 / (990e9 * 0.55) ≈ 5.8 秒；两者差距约为 3.6 倍

## Corrected Claim

基于修正后的 FLOPs (3.12 TFLOPs) 和 MFU，RTX 4090 的 Prefill 延迟 T_prefill ≈ 3.12e12 / (330e9 * 0.45) ≈ 21 秒；H100 SXM 的 T_prefill ≈ 3.12e12 / (990e9 * 0.55) ≈ 5.8 秒；两者差距约为 3.6 倍

## Evidence

先验知识/题面给定，逻辑校验通过：3.12e12 / (330e9 * 0.45) ≈ 21.05s，3.12e12 / (990e9 * 0.55) ≈ 5.75s，21.05 / 5.75 ≈ 3.66，计算与结论一致。

## Search Query

RTX 4090 H100 prefill latency 32k context LLM
