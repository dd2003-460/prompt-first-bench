# N180: 设有单笔上限的佣金结构对AOV激励的折减系数：若佣金为 $\min(r \times P_{deal}, C_{max})$，则当 $P_{deal} > C_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

设有单笔上限的佣金结构对AOV激励的折减系数：若佣金为 $\min(r \times P_{deal}, C_{max})$，则当 $P_{deal} > C_{max}/r$ 时，平台利润不再随AOV增加，边际激励为0；该阈值 $P_{threshold} = C_{max}/r$ 决定了高溢价商品是否仍受平台激励。

## Corrected Claim

设有单笔上限的佣金结构对AOV激励的折减系数：若佣金为 $\min(r \times P_{deal}, C_{max})$，则当 $P_{deal} > C_{max}/r$ 时，平台利润不再随AOV增加，边际激励为0；该阈值 $P_{threshold} = C_{max}/r$ 决定了高溢价商品是否仍受平台激励。

## Evidence

先验知识/题面给定，逻辑校验通过：根据函数 min(r*P, Cmax) 的定义，当 r*P > Cmax 即 P > Cmax/r 时，函数值恒为 Cmax，导数为0，边际激励确实为0。

## Search Query

capped commission structure threshold price marginal incentive zero
