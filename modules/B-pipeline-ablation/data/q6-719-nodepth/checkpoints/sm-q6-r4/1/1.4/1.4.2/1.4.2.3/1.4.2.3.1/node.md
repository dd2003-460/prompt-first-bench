# N709: 工作点3的每千请求回源带宽成本 C_bw_origin_per_1000req 计算为 (V_origin_day * Unit_Price_origin) /

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N235

## Claim

工作点3的每千请求回源带宽成本 C_bw_origin_per_1000req 计算为 (V_origin_day * Unit_Price_origin) / Q_day * 1000，其中 V_origin_day = Q_day * s * (1 - H_l1) + Q_day * s * H_l1 * (1 - H_l2) = 2,048,000 * 1MB * 0.2 + 2,048,000 * 1MB * 0.8 * 0.1 = 409.6GB + 163.84GB ≈ 573.44GB/天，Unit_Price_origin 为运营商回源带宽单价（典型 ¥0.1-0.2/GB），该成本项占 C_total_per_1000req 的比例通常 >50%。

## Corrected Claim

工作点3的每千请求回源带宽成本 C_bw_origin_per_1000req 计算为 (V_origin_day * Unit_Price_origin) / Q_day * 1000，其中 V_origin_day = Q_day * s * (1 - H_l1) + Q_day * s * H_l1 * (1 - H_l2) = 2,048,000 * 1MB * 0.2 + 2,048,000 * 1MB * 0.8 * 0.1 = 409.6GB + 163.84GB ≈ 573.44GB/天，Unit_Price_origin 为运营商回源带宽单价（典型 ¥0.1-0.2/GB），该成本项占 C_total_per_1000req 的比例通常 >50%。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（409.6+163.84=573.44GB），公式推导符合CDN回源带宽成本逻辑，量级合理。
