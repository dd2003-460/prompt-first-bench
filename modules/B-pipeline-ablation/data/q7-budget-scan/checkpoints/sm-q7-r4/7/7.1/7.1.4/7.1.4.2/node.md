# N622: 工作点C（1.92TB SSD）的5年电力成本 C_elec_C_5y = P_total_NVMe_C * 7200h * 5 * E_price，其中 P_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N260

## Claim

工作点C（1.92TB SSD）的5年电力成本 C_elec_C_5y = P_total_NVMe_C * 7200h * 5 * E_price，其中 P_total_NVMe_C 需基于 N282 修正后的 SSD 平均功耗（8.75W/盘）及 266 块盘计算，注意盘数加倍导致总功耗和工作点B相比有显著差异

## Corrected Claim

工作点C（1.92TB SSD）的5年电力成本 C_elec_C_5y = P_total_NVMe_C * 7200h * 5 * E_price，其中 P_total_NVMe_C 需基于 N282 修正后的 SSD 平均功耗（8.75W/盘）及 266 块盘计算，注意盘数加倍导致总功耗和工作点B相比有显著差异

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合能量=功率×时间×单价的基本物理定义，数值代入逻辑自洽（8.75W*266盘*7200h*5年*电价），且明确指出了与工作点B的差异原因（盘数加倍），无内部矛盾。
