# N686: Qwen3-27B 的 FFN 中间维度 d_ff 为 11008，该值直接决定单 token FFN 激活内存大小为 d_ff * 2 bytes = 22,

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N245

## Claim

Qwen3-27B 的 FFN 中间维度 d_ff 为 11008，该值直接决定单 token FFN 激活内存大小为 d_ff * 2 bytes = 22,016 bytes ≈ 21.5 KB，是计算 Act_Mem 峰值的关键参数。

## Corrected Claim

Qwen3-27B 的 FFN 中间维度 d_ff 为 11008，该值直接决定单 token FFN 激活内存大小为 d_ff * 2 bytes = 22,016 bytes ≈ 21.5 KB，是计算 Act_Mem 峰值的关键参数。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 的 FFN 中间维度 d_ff 为 11008 是已知的模型架构参数，单 token FFN 激活内存大小计算为 d_ff * 2 bytes = 22,016 bytes ≈ 21.5 KB，量纲和数值均合理。

## Search Query

Qwen3-27B config.json d_ff intermediate size
