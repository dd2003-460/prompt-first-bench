# N254: A100 PCIe 40GB 在 24/7 混合负载下的加权平均功耗 P_avg_A100_weighted = (P_prefill * T_prefill_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N82

## Claim

A100 PCIe 40GB 在 24/7 混合负载下的加权平均功耗 P_avg_A100_weighted = (P_prefill * T_prefill_ratio + P_decode * T_decode_ratio)，假设典型对话场景 Prefill:Decode 时间比为 1:9，则 P_avg ≈ 0.1*300W + 0.9*225W = 232.5W，修正 N82 中 350W 的高估。

## Corrected Claim

A100 PCIe 40GB 在 24/7 混合负载下的加权平均功耗 P_avg_A100_weighted = (P_prefill * T_prefill_ratio + P_decode * T_decode_ratio)，假设典型对话场景 Prefill:Decode 时间比为 1:9，则 P_avg ≈ 0.1*300W + 0.9*225W = 232.5W，修正 N82 中 350W 的高估。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 TDP为400W，Prefill阶段功耗接近TDP（~300W合理），Decode阶段受带宽限制功耗较低（~225W合理），加权平均计算逻辑自洽且量级符合工程常识。
