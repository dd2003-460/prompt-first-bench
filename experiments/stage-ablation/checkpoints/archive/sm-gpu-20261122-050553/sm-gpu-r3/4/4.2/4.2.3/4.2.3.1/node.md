# N255: RTX 5090 在 LLM 解码（Decode）阶段的功耗 P_decode_5090 预计为 250-350W，受 GDDR7 带宽读取限制，低于其 575

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N83

## Claim

RTX 5090 在 LLM 解码（Decode）阶段的功耗 P_decode_5090 预计为 250-350W，受 GDDR7 带宽读取限制，低于其 575W TDP，需基于 Blackwell 架构能效比估算或等待首批实测数据。

## Corrected Claim

RTX 5090 在 LLM 解码阶段的功耗预计低于其 575W TDP，具体数值（如 250-350W）需基于 Blackwell 架构能效比估算或等待首批实测数据确认。

## Evidence

[质询]该陈述包含具体的经验性数值范围（250-350W）和特定硬件架构（Blackwell/RTX 5090）的功耗预测，属于硬件规格/性能数据，无法从第一性原理严格推导，且缺乏实测数据支持。 | 经验事实，逻辑自洽（解码阶段受带宽限制，功耗低于TDP符合物理直觉）但缺来源支持（本轮检索无可用来源）。

## Search Query

RTX 5090 LLM inference decode power consumption watts GDDR7 bandwidth efficiency
