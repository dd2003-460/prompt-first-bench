# N49: 平台算法推荐偏差 (B_algo) 的计算公式：B_algo = (Exposure_high_price / Conversion_high_price) /

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

平台算法推荐偏差 (B_algo) 的计算公式：B_algo = (Exposure_high_price / Conversion_high_price) / (Exposure_low_price / Conversion_low_price)，其中 Exposure 和 Conversion 分别为高价组和低价组的曝光量与成交量，若 B_algo > 1.2 则确认算法偏差存在。

## Corrected Claim

平台算法推荐偏差 (B_algo) 的计算公式：B_algo = (Exposure_high_price / Conversion_high_price) / (Exposure_low_price / Conversion_low_price)，其中 Exposure 和 Conversion 分别为高价组和低价组的曝光量与成交量，若 B_algo > 1.2 则确认算法偏差存在。

## Evidence

先验知识/题面给定，逻辑校验通过
