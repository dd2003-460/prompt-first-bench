# N46: 性价比量化指标定义：定义性价比指标 Cost_Per_Token = (CapEx + 3*OpEx) / Total_Tokens_Processed_3y。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比量化指标定义：定义性价比指标 Cost_Per_Token = (CapEx + 3*OpEx) / Total_Tokens_Processed_3y。其中 Total_Tokens_Processed_3y = Throughput_Tokens_per_sec * 3600 * 24 * 365 * 3 * Utilization_Factor。该公式将硬件成本与持续推理能力挂钩，用于最终排序 [待核验]。

## Corrected Claim

在特定硬件选型评估场景中，可定义性价比指标 Cost_Per_Token = (CapEx + 3*OpEx) / Total_Tokens_Processed_3y，其中总处理量基于吞吐量、时间跨度及利用率计算。

## Evidence

[质询]该公式为特定场景下的自定义工程估算模型，并非行业通用的标准定义。参考来源主要讨论API定价或宏观经济学概念，未提供该具体公式（含3年折旧、3倍OpEx系数及利用率因子）的直接支持，存在口径混淆风险（将特定假设下的估算公式当作通用定义）。 | 逻辑自洽（量纲正确，符合TCO估算直觉），但参考来源[1][2][3]仅涉及Cost per Token的一般概念或市场价格，未直接支持该特定公式结构，属于经验事实且缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://finopsschool.com/blog/cost-per-token/&rut=4a38eb9556234889cd690f802183e25d03add8a5535585ab163477be626dd405', 'type': 'ddg', 'title': 'What is Cost per token? Meaning, Architecture, Examples, Use Cases, and ...'}
- {'url': 'https://wavect.io/zh/blog/cost-per-token-vs-cost-per-task/&rut=89d2935912452986844b4c0e223cb15d781488caab0cb8ea40437ca06781133e', 'type': 'ddg', 'title': '每任务成本：当前价格与实际用量 | Wavect'}
- {'url': 'https://analyticslegends.ai/concepts/cost-per-token-economics-2026/&rut=f8b87f4e545ea4ea980f9739f610f1f0752a1dad64fcf5f5ff302497ac7fe741', 'type': 'ddg', 'title': 'Cost-per-Token Economics 2026 — Frontier vs Open-Weights'}
