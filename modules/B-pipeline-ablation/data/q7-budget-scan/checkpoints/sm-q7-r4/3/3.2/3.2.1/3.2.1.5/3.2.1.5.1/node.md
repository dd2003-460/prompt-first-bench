# N691: HDD+SSD分层方案修正后总功耗 P_total_corrected = P_HDD(240W) + P_SSD(411.6W) + P_Controller

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N257

## Claim

HDD+SSD分层方案修正后总功耗 P_total_corrected = P_HDD(240W) + P_SSD(411.6W) + P_Controller_Corrected(145W) + P_Fans(150W) = 946.6W

## Corrected Claim

HDD+SSD分层方案修正后总功耗 P_total_corrected = P_HDD(240W) + P_SSD(411.6W) + P_Controller_Corrected(145W) + P_Fans(150W) = 946.6W

## Evidence

先验知识/题面给定，逻辑校验通过：算术求和 240 + 411.6 + 145 + 150 = 946.6 正确，各组件功耗量级符合数据中心存储系统常识。

## Search Query

storage array total power consumption calculation methodology
