# N131: HDD 单盘平均功耗 W_HDD_avg 需区分 CMR/SMR 及负载：16TB CMR HDD 空闲功耗约 4.5W，读写功耗约 8W。鉴于 80% 为冷数

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

HDD 单盘平均功耗 W_HDD_avg 需区分 CMR/SMR 及负载：16TB CMR HDD 空闲功耗约 4.5W，读写功耗约 8W。鉴于 80% 为冷数据（极低访问），假设活跃率 5%，W_HDD_avg ≈ 4.5 * 0.95 + 8 * 0.05 ≈ 4.675W。

## Corrected Claim

HDD 单盘平均功耗 W_HDD_avg 需区分 CMR/SMR 及负载：16TB CMR HDD 空闲功耗约 4.5W，读写功耗约 8W。鉴于 80% 为冷数据（极低访问），假设活跃率 5%，W_HDD_avg ≈ 4.5 * 0.95 + 8 * 0.05 ≈ 4.675W。

## Evidence

先验知识/题面给定，逻辑校验通过：16TB CMR HDD 空闲功耗约 4.5W、读写约 8W 符合行业典型数据范围，加权计算 4.5*0.95 + 8*0.05 = 4.275 + 0.4 = 4.675W 算术正确，逻辑自洽。

## Search Query

enterprise CMR HDD 16TB idle active power consumption watts
