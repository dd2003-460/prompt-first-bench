# N277: Mac Studio M2 Ultra 在 LLM 推理负载下的实际整机功耗 P_actual 约为 150W-180W（峰值），而非标称的 200W 上限；用

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

Mac Studio M2 Ultra 在 LLM 推理负载下的实际整机功耗 P_actual 约为 150W-180W（峰值），而非标称的 200W 上限；用于计算 Opex 时应采用 165W 作为均值，误差范围 ±15W

## Corrected Claim

Mac Studio M2 Ultra 在 LLM 推理负载下的实际整机功耗 P_actual 通常低于其 200W 标称上限，具体数值需依据实测数据确定，建议采用保守估计值进行 Opex 计算。

## Evidence

[质询]该陈述包含具体的经验数值（150W-180W, 165W），属于硬件功耗规格，无法从第一性原理推导。参考来源[1]为AnandTech论坛首页，未包含具体功耗数据；来源[2]为等离子体物理论文，与计算机硬件功耗完全无关。缺乏直接来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持（来源[1]、[2]均不相关或未提供具体数据）

## Search Query

Mac Studio M2 Ultra LLM inference power consumption watts

## Retrieval Sources

- {'url': 'https://anandtech.com', 'type': None, 'title': 'direct-browser: anandtech.com'}
- {'url': 'http://arxiv.org/abs/2509.02214v1', 'type': 'arxiv', 'title': 'Hot-Ion Modes in Globus-M2 and Saturation of Energy Confinement Time Scaling in '}
