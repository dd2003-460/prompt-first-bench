# N284: 自建部分回源带宽月成本 C_bw_self_month 为 V_origin_self * 30 * Unit_Price_origin，其中 Unit_Pri

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

自建部分回源带宽月成本 C_bw_self_month 为 V_origin_self * 30 * Unit_Price_origin，其中 Unit_Price_origin 为源站出口带宽单价（¥/GB，典型值 0.08-0.15，取决于带宽采购方式）

## Corrected Claim

自建部分回源带宽月成本 C_bw_self_month 为 V_origin_self * 30 * Unit_Price_origin，其中 Unit_Price_origin 为源站出口带宽单价（¥/GB，典型值 0.08-0.15，取决于带宽采购方式）

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本计算逻辑（流量×天数×单价），且0.08-0.15 ¥/GB的源站出口带宽单价符合国内云厂商及IDC市场常见价格区间。
