# N282: 回源带宽月度成本 C_bw_month (¥/月) 的具体计算示例：假设 B_peak = 35.5 Mbps，Unit_Price_95th = ¥20/Mb

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

回源带宽月度成本 C_bw_month (¥/月) 的具体计算示例：假设 B_peak = 35.5 Mbps，Unit_Price_95th = ¥20/Mbps/月，且无超量流量，则 C_bw_month = 35.5 * 20 = ¥710/月。

## Corrected Claim

回源带宽月度成本 C_bw_month (¥/月) 的具体计算示例：假设 B_peak = 35.5 Mbps，Unit_Price_95th = ¥20/Mbps/月，且无超量流量，则 C_bw_month = 35.5 * 20 = ¥710/月。

## Evidence

先验知识/题面给定，逻辑校验通过：乘法运算 35.5 * 20 = 710 正确，单位换算逻辑自洽（Mbps * ¥/Mbps/月 = ¥/月），且无超量流量假设下直接相乘符合95th计费模型的基本逻辑。
