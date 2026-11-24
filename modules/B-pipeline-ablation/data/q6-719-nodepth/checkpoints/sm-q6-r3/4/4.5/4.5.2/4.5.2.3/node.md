# N378: 两级缓存的整体回源率 H_miss_total = (1 - H_L1_self) * (1 - H_L2_self)，该值直接决定回源带宽需求 B_peak_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N116

## Claim

两级缓存的整体回源率 H_miss_total = (1 - H_L1_self) * (1 - H_L2_self)，该值直接决定回源带宽需求 B_peak_origin 和回源成本 C_origin，若 H_miss_total > 0.1，则回源成本占比将超过总带宽成本的 20%。

## Corrected Claim

两级缓存的整体回源率 H_miss_total = (1 - H_L1_self) * (1 - H_L2_self)，该值直接决定回源带宽需求 B_peak_origin 和回源成本 C_origin。回源成本占比取决于回源率及回源与边缘带宽的单位成本比，具体阈值需结合实际定价模型计算。

## Evidence

[质询]陈述中关于“H_miss_total > 0.1 则回源成本占比超过总带宽成本的 20%”的定量结论缺乏前提条件（如回源带宽与边缘带宽的单价比、流量分布等），属于经验性断言，无法仅从缓存命中率公式推导得出，存在逻辑跳跃。 | source=knowledge，公式 H_miss_total = (1 - H_L1_self) * (1 - H_L2_self) 逻辑自洽且符合两级缓存原理；但后半部分关于成本占比的定量阈值（0.1对应20%）属于经验事实，缺乏来源支持且依赖未给定的经济参数，故降级。
