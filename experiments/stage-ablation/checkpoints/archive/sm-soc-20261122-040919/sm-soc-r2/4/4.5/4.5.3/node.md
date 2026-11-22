# N93: 抽样偏差的量化评估：若平台数据存在选择偏差（如仅统计活跃卖家），则观测到的p=0.6可能偏离真实值。偏差幅度$\delta = |p_{observed} - 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

抽样偏差的量化评估：若平台数据存在选择偏差（如仅统计活跃卖家），则观测到的p=0.6可能偏离真实值。偏差幅度$\delta = |p_{observed} - p_{true}|$可通过对比平台全量数据与随机抽样数据估计。若$\delta > 0.05$，则需修正置信区间。

## Corrected Claim

抽样偏差的量化评估：若平台数据存在选择偏差（如仅统计活跃卖家），则观测到的p=0.6可能偏离真实值。偏差幅度$\delta = |p_{observed} - p_{true}|$可通过对比平台全量数据与随机抽样数据估计。若$\delta > 0.05$，则需修正置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过
