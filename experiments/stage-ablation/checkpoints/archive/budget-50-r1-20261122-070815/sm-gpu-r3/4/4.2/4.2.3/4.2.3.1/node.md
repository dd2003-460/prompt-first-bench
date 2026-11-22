# N308: NVIDIA H100 80GB SXM 的 TDP 为 700W，在 LLM 推理负载下实际功耗通常为 500W-650W，服务器基础功耗约 200W-300

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

NVIDIA H100 80GB SXM 的 TDP 为 700W，在 LLM 推理负载下实际功耗通常为 500W-650W，服务器基础功耗约 200W-300W，整机 P_avg 估算为 700W-950W

## Corrected Claim

NVIDIA H100 80GB SXM 的 TDP 为 700W，在 LLM 推理负载下实际功耗通常为 500W-650W，服务器基础功耗约 200W-300W，整机 P_avg 估算为 700W-950W

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM TDP 700W 为官方规格，推理负载功耗及整机功耗估算符合工程常识与物理直觉。

## Search Query

H100 SXM power consumption LLM inference load watts
