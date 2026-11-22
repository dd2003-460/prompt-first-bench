# N68: INT8 对称量化 (Symmetric) 与 Qwen3-27B 激活值分布的匹配度：统计 Qwen3-27B 在 32K 上下文下各层激活值的 max/mi

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16, N17, N18

## Claim

INT8 对称量化 (Symmetric) 与 Qwen3-27B 激活值分布的匹配度：统计 Qwen3-27B 在 32K 上下文下各层激活值的 max/min 分布，确认对称量化所需的 scale factor 是否导致有效位宽损失（effective bit-width < 8），从而量化理论上的精度上限。

## Corrected Claim

需统计 Qwen3-27B 在 32K 上下文下各层激活值的 max/min 分布，以确认对称量化所需的 scale factor 是否导致有效位宽损失（effective bit-width < 8），从而量化理论上的精度上限。

## Evidence

[质询]该陈述描述的是一个具体的经验性测量结果（Qwen3-27B在特定上下文下的激活值分布及量化损失），属于硬件/模型行为的具体经验事实，无法从第一性原理直接推导，且缺乏具体数值支撑，仅凭逻辑自洽不足以确认为已验证事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法外部核验具体数值或分布特征）

## Search Query

Qwen3-27B activation distribution INT8 symmetric quantization scale factor
