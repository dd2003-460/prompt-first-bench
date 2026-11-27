# N59: ΔP_actual 的量化计算式：ΔP_actual = P_new - P_old，其中 P_old 为当前高挂价下的平均成交价 (P_ask * 0.85~

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

ΔP_actual 的量化计算式：ΔP_actual = P_new - P_old，其中 P_old 为当前高挂价下的平均成交价 (P_ask * 0.85~0.875)，P_new 为打破均衡后的目标成交价 (如 P_market 或 P_ask * 0.95)，需代入具体数值计算。

## Corrected Claim

ΔP_actual 的量化计算式：ΔP_actual = P_new - P_old，其中 P_old 为当前高挂价下的平均成交价 (P_ask * 0.85~0.875)，P_new 为打破均衡后的目标成交价 (如 P_market 或 P_ask * 0.95)，需代入具体数值计算。

## Evidence

先验知识/题面给定，逻辑校验通过
