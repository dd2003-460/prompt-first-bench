# N80: 核心区域自建容量 C_core_self 的计算：核心区域流量权重 w_core=0.6，对应平均带宽 B_avg_core = 26.4 Mbps * 0.6

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

核心区域自建容量 C_core_self 的计算：核心区域流量权重 w_core=0.6，对应平均带宽 B_avg_core = 26.4 Mbps * 0.6 = 15.84 Mbps，峰值带宽 B_peak_core = 15.84 * 3 = 47.52 Mbps。假设核心区域由 6 个自建 POP 点覆盖，且目标利用率 U_core_target=60%，则所需总核心容量 C_core_self = B_peak_core / U_core_target = 47.52 / 0.6 = 79.2 Mbps。单点容量 C_pop_core = 79.2 / 6 = 13.2 Mbps。

## Corrected Claim

核心区域自建容量 C_core_self 的计算：核心区域流量权重 w_core=0.6，对应平均带宽 B_avg_core = 26.4 Mbps * 0.6 = 15.84 Mbps，峰值带宽 B_peak_core = 15.84 * 3 = 47.52 Mbps。假设核心区域由 6 个自建 POP 点覆盖，且目标利用率 U_core_target=60%，则所需总核心容量 C_core_self = B_peak_core / U_core_target = 47.52 / 0.6 = 79.2 Mbps。单点容量 C_pop_core = 79.2 / 6 = 13.2 Mbps。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算（26.4*0.6=15.84, 15.84*3=47.52, 47.52/0.6=79.2, 79.2/6=13.2）完全正确，且符合容量规划的基本逻辑（峰值带宽除以目标利用率得到所需容量）。

## Search Query

hybrid CDN capacity planning core region
