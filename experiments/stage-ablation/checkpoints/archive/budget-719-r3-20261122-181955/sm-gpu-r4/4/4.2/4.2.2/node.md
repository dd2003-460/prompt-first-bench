# N103: 在 LLM 推理负载下，GPU 的平均功耗通常为 TDP 的 60%-80%（取决于 Prefill/Decode 比例和批处理大小），因此计算年运行成本时应使

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

在 LLM 推理负载下，GPU 的平均功耗通常为 TDP 的 60%-80%（取决于 Prefill/Decode 比例和批处理大小），因此计算年运行成本时应使用 P_avg = 0.7 * P_tdp 作为估算值，而非直接乘以 TDP。

## Corrected Claim

在 LLM 推理负载下，GPU 的平均功耗通常为 TDP 的 60%-80%（取决于 Prefill/Decode 比例和批处理大小），因此计算年运行成本时应使用 P_avg = 0.7 * P_tdp 作为估算值，而非直接乘以 TDP。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU average power consumption during LLM inference vs TDP ratio
