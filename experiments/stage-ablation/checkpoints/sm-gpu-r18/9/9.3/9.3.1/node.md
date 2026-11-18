# N277: Mac Studio M2 Ultra 在 LLM 推理负载下的实际整机功耗 P_actual 约为 150W-180W（峰值），而非标称的 200W 上限；用

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

Mac Studio M2 Ultra 在 LLM 推理负载下的实际整机功耗 P_actual 约为 150W-180W（峰值），而非标称的 200W 上限；用于计算 Opex 时应采用 165W 作为均值，误差范围 ±15W

## Corrected Claim

Mac Studio M2 Ultra 在 LLM 推理负载下的实际整机功耗 P_actual 约为 150W-180W（峰值），而非标称的 200W 上限；用于计算 Opex 时应采用 165W 作为均值，误差范围 ±15W（注：具体数值需进一步实测或权威基准测试确认）

## Evidence

[质询]该陈述属于具体的硬件功耗经验数据，参考来源完全不相关，且缺乏直接的外部来源支持来验证具体的数值范围（150W-180W）和均值（165W）。 | 经验事实，逻辑自洽但缺来源支持（参考来源[1]为等离子体物理论文，与Mac Studio功耗无关）

## Search Query

Mac Studio M2 Ultra LLM inference power consumption watts

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2509.02214v1', 'type': 'arxiv', 'title': 'Hot-Ion Modes in Globus-M2 and Saturation of Energy Confinement Time Scaling in '}
