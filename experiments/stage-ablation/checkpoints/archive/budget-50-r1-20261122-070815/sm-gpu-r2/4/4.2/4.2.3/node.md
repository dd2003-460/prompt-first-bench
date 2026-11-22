# N107: NVIDIA H100 (80GB SXM) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 750W (GPU TDP 700W + 系统开销 ~7%

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

NVIDIA H100 (80GB SXM) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 750W (GPU TDP 700W + 系统开销 ~7%)，其 FP8 原生支持可能降低单位 token 能耗

## Corrected Claim

NVIDIA H100 (80GB SXM) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 750W (GPU TDP 700W + 系统开销 ~7%)，其 FP8 原生支持可能降低单位 token 能耗

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM TDP 700W 为官方规格，整机功耗 750W 符合工程常识，FP8 降低能耗符合计算原理。
