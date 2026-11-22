# N220: H100 SXM 在 Qwen3-27B 推理负载下的平均功耗修正系数：实际平均功耗 P_avg = P_peak * Load_Factor。其中 P_pea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

H100 SXM 在 Qwen3-27B 推理负载下的平均功耗修正系数：实际平均功耗 P_avg = P_peak * Load_Factor。其中 P_peak = 700W (TDP)，Load_Factor 在持续 Decode 阶段通常为 0.7-0.85 (基于 H100 能效曲线及 LLM 推理负载特征)，在 Prefill 阶段接近 1.0。若假设 80% 时间处于 Decode，20% 处于 Prefill，则加权平均 Load_Factor ≈ 0.8 * 0.75 + 0.2 * 1.0 = 0.8。

## Corrected Claim

H100 SXM 在 Qwen3-27B 推理负载下的平均功耗修正系数：实际平均功耗 P_avg = P_peak * Load_Factor。其中 P_peak = 700W (TDP)，Load_Factor 在持续 Decode 阶段通常为 0.7-0.85 (基于 H100 能效曲线及 LLM 推理负载特征)，在 Prefill 阶段接近 1.0。若假设 80% 时间处于 Decode，20% 处于 Prefill，则加权平均 Load_Factor ≈ 0.8 * 0.75 + 0.2 * 1.0 = 0.8。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 TDP 700W 为公开规格，LLM 推理中 Decode 阶段功耗低于 Prefill 符合硬件能效特性，加权平均计算逻辑自洽且数值量级合理。

## Search Query

H100 SXM average power consumption LLM inference load factor
