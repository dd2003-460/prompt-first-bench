# N222: 峰值小时请求量 L_peak_hour 的计算公式：L_peak_hour = Mean_L_hour * Peak_Factor，其中 Mean_L_hour

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

峰值小时请求量 L_peak_hour 的计算公式：L_peak_hour = Mean_L_hour * Peak_Factor，其中 Mean_L_hour = 20,000,000,000 bytes / 24 h ≈ 833 MB/h，需转换为请求数。

## Corrected Claim

峰值小时请求量 L_peak_hour 的计算公式：L_peak_hour = Mean_L_hour * Peak_Factor，其中 Mean_L_hour = 20,000,000,000 bytes / 24 h ≈ 833 MB/h，需转换为请求数。

## Evidence

先验知识/题面给定，逻辑校验通过：20,000,000,000 bytes / 24 h ≈ 833.33 MB/h，数值量级与单位换算正确，公式结构符合常规负载估算逻辑。
