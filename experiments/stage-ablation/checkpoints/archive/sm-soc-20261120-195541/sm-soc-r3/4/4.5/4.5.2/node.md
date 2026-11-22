# N53: ARPU异质性修正：区分‘高挂价卖家’（挂价>市场均价15%）与‘普通卖家’的ARPU差异，若高挂价卖家ARPU是普通卖家的1.5倍，则同等流失率下对平台LTV

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

ARPU异质性修正：区分‘高挂价卖家’（挂价>市场均价15%）与‘普通卖家’的ARPU差异，若高挂价卖家ARPU是普通卖家的1.5倍，则同等流失率下对平台LTV的损害权重需乘以1.5

## Corrected Claim

ARPU异质性修正：区分‘高挂价卖家’与‘普通卖家’的ARPU差异，若高挂价卖家ARPU是普通卖家的K倍（K>1），则同等流失率下对平台LTV的损害权重需乘以K。

## Evidence

父节点级核验未通过：有冗余（子节点本质上是对同一个数学公式（LTV损害权重计算）在不同参数组合下的具体数值实例化。虽然它们在业务场景上（高/低活跃、高/低溢价）形成了正交的象限，且覆盖了从保守到极端的情况，但它们并非独立的逻辑分支，而是同一计算逻辑的冗余展开。）

## Search Query

high listing price sellers ARPU comparison marketplace data analysis
