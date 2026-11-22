# N315: NVIDIA H100 PCIe 80GB 的 TDP 为 350W (PCIe 版本，非 SXM 的 700W)，在 LLM Decode 负载下平均功耗 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

NVIDIA H100 PCIe 80GB 的 TDP 为 350W (PCIe 版本，非 SXM 的 700W)，在 LLM Decode 负载下平均功耗 P_avg_H100 约为 280-320W，保守取 300W 用于 TCO 计算，修正原 N107 中 400W 的高估。

## Corrected Claim

NVIDIA H100 PCIe 80GB 的 TDP 为 350W (PCIe 版本，非 SXM 的 700W)，在 LLM Decode 负载下平均功耗 P_avg_H100 约为 280-320W，保守取 300W 用于 TCO 计算，修正原 N107 中 400W 的高估。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA H100 PCIe 80GB 的官方 TDP 确为 350W（SXM 为 700W），LLM Decode 负载下平均功耗 280-320W 符合工程经验，取 300W 用于 TCO 计算合理且修正了原 400W 的高估。
