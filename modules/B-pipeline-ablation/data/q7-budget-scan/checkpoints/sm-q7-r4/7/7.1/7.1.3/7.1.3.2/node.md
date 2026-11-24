# N619: 工作点B（3.84TB SSD）的5年电力成本 C_elec_B_5y = P_total_NVMe_B * 7200h * 5 * E_price，其中 P_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N259

## Claim

工作点B（3.84TB SSD）的5年电力成本 C_elec_B_5y = P_total_NVMe_B * 7200h * 5 * E_price，其中 P_total_NVMe_B 需基于 N275/N282 修正后的 SSD 平均功耗（约 8.75W/盘）及 133 块盘计算，修正自矛盾检测中 N282 与 N265 的空闲功耗冲突，采用 N265 的 1.0-1.5W 空闲值进行加权

## Corrected Claim

工作点B（3.84TB SSD）的5年电力成本 C_elec_B_5y = P_total_NVMe_B * 7200h * 5 * E_price，其中 P_total_NVMe_B 需基于 N275/N282 修正后的 SSD 平均功耗（约 8.75W/盘）及 133 块盘计算，修正自矛盾检测中 N282 与 N265 的空闲功耗冲突，采用 N265 的 1.0-1.5W 空闲值进行加权

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合能量=功率×时间×单价的基本物理定义，数值量级（8.75W/盘，133盘，5年）在SSD集群能耗估算中合理，且明确指出了基于前序节点（N265/N282）的修正逻辑，内部自洽。
