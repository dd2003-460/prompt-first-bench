# N26: 高性低成工作点：本地NVMe SSD阵列在RTO<5min、温数据IOPS>1M IOPS场景下最优，5年TCO约为¥8500/TB·年（含硬件¥6000+电力

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

高性低成工作点：本地NVMe SSD阵列在RTO<5min、温数据IOPS>1M IOPS场景下最优，5年TCO约为¥8500/TB·年（含硬件¥6000+电力¥800+运维¥1200+RTO代价¥500），但仅当业务SLA要求极高且数据量<200TB时可行，500TB规模下硬件成本超标3x

## Corrected Claim

本地NVMe SSD阵列在RTO<5min、温数据IOPS>1M IOPS场景下性能最优，但5年TCO极高（通常远超¥8500/TB·年），仅当业务SLA要求极高且数据量较小（如<50TB）时可行，大规模（如500TB）下硬件成本通常不可接受。

## Evidence

[质询]数值量级与成本结构存在严重逻辑矛盾：1M IOPS 的 NVMe 阵列硬件成本极高，5年 TCO 折合 ¥8500/TB·年（即 ¥42,500/TB 总成本）远低于当前企业级 NVMe SSD 的市场单价（通常 >¥10,000/TB 仅硬件），且 500TB 规模下硬件成本超标 3x 的结论与线性扩展逻辑不符（若 200TB 可行，500TB 成本应约为 2.5 倍，而非 3 倍超标导致不可行，除非有非线性惩罚，但陈述未说明）。 | 先验知识/题面给定，逻辑校验未通过：TCO 数值远低于硬件成本下限，且规模扩展逻辑不自洽。
