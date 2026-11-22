# N53: ARPU异质性修正：区分‘高挂价卖家’（挂价>市场均价15%）与‘普通卖家’的ARPU差异，若高挂价卖家ARPU是普通卖家的1.5倍，则同等流失率下对平台LTV

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

ARPU异质性修正：区分‘高挂价卖家’（挂价>市场均价15%）与‘普通卖家’的ARPU差异，若高挂价卖家ARPU是普通卖家的1.5倍，则同等流失率下对平台LTV的损害权重需乘以1.5

## Corrected Claim

ARPU异质性修正：区分‘高挂价卖家’与‘普通卖家’的ARPU差异，若高挂价卖家ARPU是普通卖家的K倍（K>1），则同等流失率下对平台LTV的损害权重需乘以K。

## Evidence

[质询]该陈述包含具体的经验性假设（高挂价卖家ARPU是普通卖家的1.5倍），这属于市场经验数据而非第一性原理可推导的数学或逻辑事实，且缺乏来源支持该具体倍数关系。 | 逻辑推导部分（LTV损害权重与ARPU成正比）自洽，但'1.5倍'这一具体数值为经验事实，检索无可用来源支持，依据经验事实排除条款降级。

## Search Query

high listing price sellers ARPU comparison marketplace data analysis
