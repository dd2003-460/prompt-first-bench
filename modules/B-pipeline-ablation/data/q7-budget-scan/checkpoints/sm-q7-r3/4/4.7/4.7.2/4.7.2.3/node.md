# N228: 修正后的云带宽租用成本 C_bw = B_required * P_link_daily * (T_transfer / 24h)。若使用阿里云专线，B=11.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

修正后的云带宽租用成本 C_bw = B_required * P_link_daily * (T_transfer / 24h)。若使用阿里云专线，B=11.17Gbps，P=¥166/Gbps/天，T=4h，则 C_bw = 11.17 * 166 * (4/24) ≈ ¥310。若使用N90原假设的¥100/Gbps/天，则 C_bw ≈ ¥186。两者均远低于N90原claim的¥19,000，原claim可能误用了月度费率或未正确除以天数

## Corrected Claim

修正后的云带宽租用成本 C_bw = B_required * P_link_daily * (T_transfer / 24h)。若使用阿里云专线，B=11.17Gbps，P=¥166/Gbps/天，T=4h，则 C_bw = 11.17 * 166 * (4/24) ≈ ¥310。若使用N90原假设的¥100/Gbps/天，则 C_bw ≈ ¥186。两者均远低于N90原claim的¥19,000，原claim可能误用了月度费率或未正确除以天数

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 11.17 * 166 * (4/24) ≈ 310.5 和 11.17 * 100 * (4/24) ≈ 186.2 均准确无误，量纲与逻辑自洽。
