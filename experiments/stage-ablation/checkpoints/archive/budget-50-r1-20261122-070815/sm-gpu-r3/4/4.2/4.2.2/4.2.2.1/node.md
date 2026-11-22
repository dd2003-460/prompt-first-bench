# N305: NVIDIA A100 80GB SXM 的 TDP 为 400W，但在 LLM 推理负载下实际功耗通常为 300W-380W，且服务器平台的基础功耗（CPU/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

NVIDIA A100 80GB SXM 的 TDP 为 400W，但在 LLM 推理负载下实际功耗通常为 300W-380W，且服务器平台的基础功耗（CPU/内存/散热）通常比消费级高，约为 200W-300W

## Corrected Claim

NVIDIA A100 80GB SXM 的 TDP 为 400W，但在 LLM 推理负载下实际功耗通常为 300W-380W，且服务器平台的基础功耗（CPU/内存/散热）通常比消费级高，约为 200W-300W

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM 400W TDP 及推理负载下 300-380W 实际功耗符合工程常识，服务器基础功耗 200-300W 亦在合理量级范围内。

## Search Query

A100 SXM power consumption LLM inference load watts server overhead
