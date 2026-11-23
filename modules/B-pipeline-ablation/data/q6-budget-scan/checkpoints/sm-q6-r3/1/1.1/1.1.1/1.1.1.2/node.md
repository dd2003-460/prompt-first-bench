# N115: Top 10 省份流量占比 P_core_top10 随平台 ARPU 地域差异修正：P_core_top10 = P_base * (1 + k_arpu *

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

Top 10 省份流量占比 P_core_top10 随平台 ARPU 地域差异修正：P_core_top10 = P_base * (1 + k_arpu * Var_ARPU_geo)，其中 Var_ARPU_geo 为省份 ARPU 变异系数，k_arpu 为敏感度系数（通常 0.2-0.5）；高 ARPU 地域（京沪浙）占比每增加 1%，P_core_top10 增加约 0.3-0.5%。

## Corrected Claim

Top 10 省份流量占比 P_core_top10 可随平台 ARPU 地域差异进行修正，修正幅度与省份 ARPU 变异系数及敏感度系数正相关；具体系数 k_arpu 及边际效应需根据特定平台的历史数据回归确定，通常经验值在 0.2-0.5 区间，但非通用常数。

## Evidence

[质询]该公式为经验性工程估算模型，缺乏通用的第一性原理推导基础；k_arpu 取值范围（0.2-0.5）及边际效应（0.3-0.5%）属于特定业务场景下的经验参数，无法从数学公理或物理定律中严格推出，且不同平台/行业差异巨大，存在口径混淆风险。 | source=knowledge，逻辑自洽（量纲合理，修正方向符合直觉），但属于经验事实/工程参数，无外部来源支持，依据经验事实排除条款降级。

## Search Query

china provincial ARPU variance impact on CDN traffic distribution model
