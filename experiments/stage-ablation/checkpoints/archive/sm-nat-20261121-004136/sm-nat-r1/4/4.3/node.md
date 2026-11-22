# N17: 有效命中率折损因子 Discount_Factor = 1 - P_invalid * (1 - Hit_Rate_Original)，其中 Hit_Rate_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

有效命中率折损因子 Discount_Factor = 1 - P_invalid * (1 - Hit_Rate_Original)，其中 Hit_Rate_Original 为无更新时的 LRU 字节命中率（来自子问 a 的结果），P_invalid 来自 N6。

## Corrected Claim

有效命中率折损因子 Discount_Factor = 1 - P_invalid * (1 - Hit_Rate_Original)，其中 Hit_Rate_Original 为无更新时的 LRU 字节命中率（来自子问 a 的结果），P_invalid 来自 N6。

## Evidence

先验知识/题面给定，逻辑校验通过
